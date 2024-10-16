Here’s the revised README file with the installation commands presented in bullet points without bash formatting:

---

# **AI-Powered Chatbot with Text Extraction Capabilities**

This project combines various technologies to create an AI-powered chatbot that can extract text from images, PDFs, and Word documents. It uses **Tesseract OCR** for image text extraction, **PyMuPDF** for PDFs, **python-docx** for Word documents, and **OpenAI** to generate AI-driven responses. The chatbot is built using **Gradio** for its user interface and integrated with **Groq** for optimized performance.

## **Features**
- **Multi-file Support**: Upload images, PDFs, and Word documents for text extraction.
- **AI-powered Conversational Interface**: Get responses using natural language processing via OpenAI.
- **Performance Optimization**: Integrates with Groq for fast and efficient processing.

## **Requirements**
Before running the project, make sure you have the following installed:
- Python 3.6 or higher
- pip (Python package installer)

## **Installation**

1. **Tesseract OCR Installation**  
   Download and install Tesseract OCR for image text extraction:
   - Visit the official [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).
   - Download the latest installer (e.g., `tesseract-ocr-w32-setup-v5.4.0.20220606.exe`).

2. **Required Python Libraries**  
   Use `pip` to install the necessary libraries:
   - Install PyMuPDF for PDF text extraction.
   - Install python-docx for extracting text from Word files.
   - Install Gradio version 3.39.0.
   - Uninstall the latest version of Typer, then install a compatible version:
     - `pip uninstall typer`
     - `pip install "typer<0.10.0,>=0.3.0"`
   - Check for any dependency issues: `pip check`
   - Upgrade pip: `python.exe -m pip install --upgrade pip`
   - Install Swarmauri and python-dotenv:
     - `pip install swarmauri[full]==0.4.1`
     - `pip install python-dotenv`
   - Install Groq.
   - Install OpenAI version 0.28 and upgrade to the latest version:
     - `pip install openai==0.28`
     - `pip install --upgrade openai`

3. **Virtual Environment Setup**  
   It is recommended to use a virtual environment for managing dependencies:
   - Create and activate a virtual environment suitable for your operating system.

## **Usage**
Once everything is installed and set up:

1. Run the chatbot script to start the Gradio interface.
2. The chatbot will allow users to upload images, PDFs, or Word documents, extract text from them, and receive responses generated using OpenAI.

