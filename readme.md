AI-Powered Chatbot with Text Extraction Capabilities
This project creates an AI-powered chatbot that allows users to upload images, PDF files, and Word documents. The chatbot extracts text from these files using Tesseract OCR, PyMuPDF, and python-docx, and leverages OpenAI to generate responses. The chatbot is built with Gradio for an interactive user interface, with performance optimization via Groq.

Features
Text Extraction from Images using Tesseract OCR.
Text Extraction from PDFs using PyMuPDF.
Text Extraction from Word Files using python-docx.
AI-Powered Chatbot Responses via OpenAI.
Interactive User Interface built with Gradio.
Groq Integration for faster inference and performance.
Prerequisites
Ensure that Python 3.6+ is installed on your system.

1. Tesseract OCR Installation
Download and install Tesseract OCR for image-to-text extraction:

Visit the official Tesseract GitHub repository.
Download the latest stable version of the .exe installer for Windows (e.g., tesseract-ocr-w32-setup-v5.4.0.20220606.exe).
2. Python Libraries
Install the required libraries:

PyMuPDF for PDF text extraction:

bash
Copy code
pip install PyMuPDF
python-docx for extracting text from Word files:

bash
Copy code
pip install python-docx
pytesseract for using Tesseract OCR with Python:

bash
Copy code
pip install pytesseract
Gradio for building the chatbot interface:

bash
Copy code
pip install gradio==3.39.0
If you encounter issues with typer, uninstall and install a compatible version:

bash
Copy code
pip uninstall typer
pip install "typer<0.10.0,>=0.3.0"
OpenAI for AI-powered responses:

bash
Copy code
pip install openai==0.28
pip install --upgrade openai
Groq for optimizing model inference:

bash
Copy code
pip install groq
Swarmauri and python-dotenv for environment configuration and performance:

bash
Copy code
pip install swarmauri[full]==0.4.1 python-dotenv
3. Additional Setup
Upgrade pip if needed:

bash
Copy code
python.exe -m pip install --upgrade pip
Check Dependencies: Make sure all dependencies are correctly installed:

bash
Copy code
pip check
Virtual Environment Setup
It's recommended to use a virtual environment for dependency management:

Create the environment:

bash
Copy code
python -m venv myenv
Activate the environment:

On Windows:

bash
Copy code
myenv\Scripts\activate
On macOS/Linux:

bash
Copy code
source myenv/bin/activate
Running the Chatbot
Once the environment is set up and the dependencies are installed, you can run the chatbot:

Start the Gradio interface by running the script:

bash
Copy code
python chatbot.py
The chatbot will allow users to upload images, PDFs, or Word files, extract the text from the uploaded file, and generate a response using OpenAI.

