from dotenv import load_dotenv  # Load environment variables from .env file
from PIL import Image  # Import the Python Imaging Library (PIL) for image processing
import pytesseract  # Import pytesseract for Optical Character Recognition (OCR)
import pandas as pd  # Import pandas for data manipulation and analysis
import os  # Import os for interacting with the operating system
import fitz  # Import PyMuPDF for handling PDF documents
import gradio as gr  # Import Gradio for creating web interfaces
from docx import Document  # Import Document for reading Word files
from swarmauri.standard.llms.concrete.GroqModel import GroqModel  # Import GroqModel for LLM functionality
from swarmauri.standard.messages.concrete.SystemMessage import SystemMessage  # Import SystemMessage for conversation context
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent  # Import agent for conversation handling
from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation  # Import conversation management class

# Load environment variables from the .env file
load_dotenv()

# Fetch the API key from environment variables
API_KEY = os.getenv("GROQ_API_KEY")  # Get the API key from the environment
if API_KEY is None:  # Check if the API key is missing
    raise ValueError("API key not found. Please check your .env file.")  # Raise an error if the key is not found

# Add the Tesseract path for OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Set the Tesseract command path

# Initialize the GroqModel with the API key to access allowed models
llm = GroqModel(api_key=API_KEY)

# Get the available models from the llm instance
allowed_models = llm.allowed_models  # Fetch the list of models available for use

# Initialize a MaxSystemContextConversation instance for managing conversations
conversation = MaxSystemContextConversation()

def analyze_image(image):
    """Extract text from an image using OCR."""
    text = pytesseract.image_to_string(image)  # Use pytesseract to convert image to text
    return text  # Return the extracted text

def analyze_pdf(file):
    """Extract text from a PDF file."""
    text = ""  # Initialize an empty string for text extraction
    pdf_document = fitz.open(file.name)  # Open the PDF document
    for page in pdf_document:  # Iterate through each page in the PDF
        text += page.get_text()  # Extract text from the page and append it to the text string
    pdf_document.close()  # Close the PDF document
    return text  # Return the extracted text

def analyze_word(file):
    """Extract text from a Word document."""
    doc = Document(file.name)  # Load the Word document
    text = ""  # Initialize an empty string for text extraction
    for paragraph in doc.paragraphs:  # Iterate through each paragraph in the document
        text += paragraph.text + "\n"  # Append paragraph text to the string with a newline
    return text  # Return the extracted text

def analyze_file(file):
    """Determine the file type and extract text accordingly."""
    if file.name.endswith('.txt'):  # Check if the file is a text file
        with open(file.name, 'r') as f:  # Open the text file for reading
            return f.read()  # Return the content of the file
    elif file.name.endswith('.csv'):  # Check if the file is a CSV file
        df = pd.read_csv(file.name)  # Read the CSV file into a DataFrame
        return df.head().to_string()  # Return the first few rows of the DataFrame as a string
    elif file.name.endswith('.pdf'):  # Check if the file is a PDF file
        return analyze_pdf(file)  # Call the analyze_pdf function
    elif file.name.endswith('.docx'):  # Check if the file is a Word document
        return analyze_word(file)  # Call the analyze_word function
    return "Unsupported file type."  # Return an error message for unsupported file types

def handle_feedback(user_feedback, history):
    """Log user feedback and interaction history to a text file."""
    with open("feedback.txt", "a", encoding='utf-8') as f:  # Open feedback.txt in append mode
        f.write(f"User Feedback: {user_feedback}\n")  # Write user feedback to the file
        f.write("User Interaction History:\n")  # Write a header for interaction history
        for entry in history:  # Iterate through interaction history
            f.write(f"User: {entry[0]}\nAgent: {entry[1]}\n")  # Write each entry to the file
        f.write("\n" + "-"*40 + "\n\n")  # Add a separator for clarity
    
    return "Thank you for your feedback!"  # Return a thank you message

def converse(input_text, history, system_context="", model_name="", image=None, file=None, feedback=""):
    """Process user input, extract text from files, and interact with the model."""
    if history is None:  # Check if the history is None
        history = []  # Initialize an empty history list

    # Extract text from the image if provided
    if image is not None:  # Check if an image is uploaded
        image_text = analyze_image(image)  # Analyze the image for text
        print(f"Extracted Text from Image: {image_text}")  # Debugging output
        input_text += " " + image_text  # Append extracted text to user input

    # Extract text from the file if provided
    if file is not None:  # Check if a file is uploaded
        file_content = analyze_file(file)  # Analyze the file for text
        print(f"Extracted Text from File: {file_content}")  # Debugging output
        input_text += " " + file_content  # Append extracted text to user input

    # Clean up the input text
    input_text = str(input_text).strip()  # Convert to string and strip whitespace
    
    # Check if the input text is meaningful
    if not input_text or len(input_text) < 5:  # Ensure input text has sufficient length
        return "Please enter a message or upload a file with valid content.", history, "", ""  # Return error message if not

    # Debugging output before calling the model
    print(f"Final Input Text: {input_text}")  # Debugging output

    # Initialize the model and agent
    llm = GroqModel(api_key=API_KEY, name=model_name)  # Create a GroqModel instance with the selected model
    agent = SimpleConversationAgent(llm=llm, conversation=conversation)  # Create an agent for handling the conversation
    agent.conversation.system_context = SystemMessage(content=system_context)  # Set system context

    try:
        # Call the model and get the response
        result = agent.exec(input_text)  # Execute the agent with the input text
        
        # Debugging output for model response
        print(f"Model Response: {result}")  # Debugging output

        # Ensure response is meaningful
        if isinstance(result, str) and result.strip():  # Check if result is a non-empty string
            result_str = result  # Assign valid response to result_str
        else:
            result_str = "The model did not return a valid response. Please try again."  # Assign error message

    except Exception as e:  # Handle any exceptions that may occur
        result_str = f"An error occurred: {str(e)}"  # Set result_str to the error message
        print(result_str)  # Debugging output

    # Clean up the response for better display
    result_str = result_str.replace("\n", " ").replace("\r", " ")  # Remove newlines and carriage returns

    # Append interaction to history
    history.append((input_text, result_str))  # Add current interaction to history

    # Handle feedback if provided
    feedback_response = ""
    if feedback:  # Check if feedback is provided
        feedback_response = handle_feedback(feedback, history)  # Call handle_feedback function

    # Format history for the interface
    formatted_history = "\n".join([f"Q: {entry[0]}\nA: {entry[1]}" for entry in history])  # Format history as a string

    return result_str, history, feedback_response, formatted_history  # Return response, updated history, feedback response, and formatted history

# Gradio setup remains the same

# Adjust the clear function to reset all necessary outputs
def clear_interface():
    """Reset all input and output fields to their default state."""
    return (
        "",      # User Input (Textbox)
        [],     # History State (State)
        "",      # System Context (Textbox)
        allowed_models[0],  # Model Name (Dropdown) - Set default model
        None,    # Image Input (Image) - Reset image input
        None,    # File Input (File) - Reset file input
        "",      # Feedback Input (Textbox) - Reset feedback input
        "",      # Response Output (Textbox) - Reset response output
        "",      # Feedback Response Output (Textbox) - Reset feedback response output
        ""       # Conversation History Output (Textbox) - Reset conversation history output
    )



# Gradio UI layout
with gr.Blocks() as demo:
    gr.Markdown("## AI Document Analysis with Groq")  # Title
    with gr.Row():  # Row layout for inputs
        user_input = gr.Textbox(label="User Input")  # User input textbox
        model_name = gr.Dropdown(choices=allowed_models, label="Select Model")  # Model selection dropdown
    with gr.Row():  # Row layout for image upload and file upload
        image_input = gr.Image(type="pil", label="Upload Image")  # Image upload field
        file_input = gr.File(label="Upload File")  # File upload field
    with gr.Row():  # Row layout for system context and feedback
        system_context_input = gr.Textbox(label="System Context")  # System context input
        feedback_input = gr.Textbox(label="User Feedback")  # Feedback input
    submit_button = gr.Button("Submit")  # Submit button
    clear_button = gr.Button("Clear")  # Clear button
    response_output = gr.Textbox(label="Response")  # Response output field
    feedback_response_output = gr.Textbox(label="Feedback Response")  # Feedback response output field
    history_output = gr.Textbox(label="Conversation History")  # History output field

    # Define the event handlers
    submit_button.click(converse, 
        inputs=[user_input, "state", system_context_input, model_name, image_input, file_input, feedback_input], 
        outputs=[response_output, "state", feedback_response_output, history_output]
    )  # Handle submit button click
    clear_button.click(clear_interface, outputs=[user_input, "state", system_context_input, model_name, image_input, file_input, feedback_input, response_output, feedback_response_output, history_output])  # Handle clear button click

# Launch the Gradio interface
demo.launch(share=True)  # Launch the app and provide a shareable link


