                    AI-Powered Chatbot with Text Extraction Capabilities
This project creates an AI-powered chatbot that allows users to upload images, PDF files, and Word documents. The chatbot extracts text from these files using Tesseract OCR, PyMuPDF, and python-docx, and leverages OpenAI to generate responses. The chatbot is built with Gradio for an interactive user interface, with performance optimization via Groq.

Features
    Text extraction from images using Tesseract OCR.
    Text extraction from PDFs using PyMuPDF.
    Text extraction from Word files using python-docx.
    AI-powered chatbot responses via OpenAI.
    Interactive user interface built with Gradio.
    Groq integration for faster inference and performance.
    Prerequisites
    Ensure that Python 3.6 or newer is installed on your system.

1. Tesseract OCR Installation
    Download and install Tesseract OCR for image-to-text extraction. Visit the official Tesseract GitHub repository and download the latest stable version of the .exe installer for Windows (for example, tesseract-ocr-w32-setup-v5.4.0.20220606.exe).

2. Python Libraries
    Install the required Python libraries:

    Install PyMuPDF for PDF text extraction.
    Install python-docx for extracting text from Word files.
    Install pytesseract to use Tesseract OCR with Python.
    Install Gradio to build the chatbot interface.
    Install OpenAI for AI-powered responses.
    Install Groq for optimizing model inference.
    Install Swarmauri and python-dotenv for environment configuration and performance.
3. Additional Setup
    Make sure to upgrade pip if needed and check for any dependency issues to ensure all required libraries are correctly installed.

Virtual Environment Setup
It is recommended to use a virtual environment to manage your project's dependencies. Create a virtual environment, and then activate it based on your operating system.

Running the Chatbot
Once everything is set up, you can run the chatbot by executing the relevant script. The chatbot will allow users to upload images, PDFs, or Word files, extract the text from the uploaded file, and generate a response using OpenAI.