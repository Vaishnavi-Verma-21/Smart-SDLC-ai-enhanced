# Smart-SDLC-ai-enhanced

SmartSDLC is an AI-powered platform designed to streamline and automate key stages of the software development lifecycle. It leverages modern AI models to assist with requirement analysis, code generation, bug fixing, test case generation, code summarization, and AI chatbot support.

---

## 🚀 Features

- **PDF Requirement Extraction**: Upload a PDF file to automatically extract and analyze software requirements.
- **AI-Driven Code Tools**:
  - 🔧 Code Generation
  - 🐞 Bug Fixing
  - ✅ Unit Test Case Generation
  - 📄 Code Summarization
- **Interactive AI Chatbot**: Get real-time help with software development queries.
- **Secure User Authentication**: Register/login functionality with hashed passwords.
- **Modern Tech Stack**:
  - Backend: FastAPI
  - Frontend: Streamlit
  - Auth: JWT-based
  - AI: Hugging Face Inference API
  - Storage: In-memory (for demo)

---

## 🛠️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/SmartSDLC-ai-enhanced.git
cd SmartSDLC-ai-enhanced
```

2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Create .env File
Create a .env file in the root directory and add your Hugging Face token:
```bash
HF_TOKEN=your_huggingface_token
```

6. Run the App
```bash
streamlit run app.py
```
