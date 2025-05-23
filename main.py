import streamlit as st
import PyPDF2
import io
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Page settings
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📋", layout="centered")

# === Minimal Styling ===
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #0f172a;
            color: #e2e8f0;
        }

        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            text-align: center;
            font-size: 16px;
            color: #94a3b8;
            margin-bottom: 2rem;
        }

        .stTextInput>div>div>input {
            background-color: #1e293b;
            color: #f1f5f9;
            border-radius: 6px;
            border: 1px solid #334155;
        }

        .stButton>button {
            background-color: #3b82f6;
            color: white;
            font-weight: 600;
            padding: 10px 20px;
            border-radius: 6px;
            border: none;
        }

        .analysis-section {
            margin-top: 2rem;
            padding: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# === Header ===
st.markdown('<div class="main-title">📋 AI Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload your resume and get AI-generated suggestions to improve it.</div>', unsafe_allow_html=True)

# === Inputs ===
uploaded_file = st.file_uploader("📄 Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("🎯 Job Role (Optional)", placeholder="e.g. Backend Developer")
analyze = st.button("🚀 Analyze Resume")

# === Text Extraction ===
def extract_text_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def extract(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

# === Resume Analysis ===
if analyze and uploaded_file:
    try:
        file_content = extract(uploaded_file)
        if not file_content.strip():
            st.error("❌ The uploaded file is empty or unreadable.")
            st.stop()

        prompt = f"""
        Please analyze this resume and provide feedback focused on:
        1. Content clarity and impact
        2. Skills presentation
        3. Relevance of experience for {'the role of ' + job_role if job_role else 'general job applications'}

        Resume:
        {file_content}

        Provide structured recommendations in clear formatting.
        """

        model = ChatGroq(
            model_name="llama3-8b-8192",
            temperature=0.7,
            api_key=GROQ_API_KEY
        )

        response = model.invoke([HumanMessage(content=prompt)])

        # === Output ===
        st.markdown('<div class="analysis-section">', unsafe_allow_html=True)
        st.markdown("### 📊 Resume Feedback")
        st.markdown(response.content)
        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")