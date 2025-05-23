# AI Resume Analyzer 📋

AI Resume Analyzer is a Streamlit web application that allows users to upload their resumes (PDF or TXT) and receive AI-generated feedback to improve their resume content. It provides actionable insights focused on content clarity, skills presentation, and relevance of experience based on a specified job role or general job applications.

## Features

- Upload resume files in PDF or TXT formats
- Optional input for target job role to tailor the analysis
- Extracts text content from resumes using PyPDF2
- Uses AI (via Groq's Llama3 model) to generate detailed, structured feedback
- Clean and user-friendly interface with custom dark theme styling
- Instant, interactive resume analysis for better job application success

## Technologies Used

- [Streamlit](https://streamlit.io/) for the web interface
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF text extraction
- [Langchain](https://python.langchain.com/) & Groq API for AI-based resume analysis
- Python 3.x
- dotenv for environment variable management

## Getting Started

### Prerequisites

- Python 3.7+
- Groq API key (set as `GROQ_API_KEY` in a `.env` file)
