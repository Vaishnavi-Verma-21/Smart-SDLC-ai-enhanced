import requests

# Update this if your FastAPI backend is running on a different host or port
BASE_URL = "http://127.0.0.1:9000"

def post(endpoint: str, data: dict):
    try:
        response = requests.post(f"{BASE_URL}{endpoint}", json=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
      
def post_file(endpoint: str, file):
    try:
        files = {"file": file}
        response = requests.post(f"{BASE_URL}{endpoint}", files=files)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def submit_feedback(feedback_data: dict):
    """
    Sends feedback data to the FastAPI backend.
    """
    return post("/feedback/", feedback_data)
  
def submit_feedback(feedback_data: dict):
    return post("/feedback/", feedback_data)

# ✅ 🔽 INSERT THESE HERE (after `submit_feedback`)
def generate_code(prompt_text: str):
    return post("/ai/generate-code", {"prompt": prompt_text})

def ask_chatbot(question: str):
    return post("/ai/chatbot", {"question": question})

def upload_pdf(file):
    return post_file("/ai/upload-pdf", file)
  
def send_chat_message(message: str):
    return post("/chat/chat", {"message": message}) 










