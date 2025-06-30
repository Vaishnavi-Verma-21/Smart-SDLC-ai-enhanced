import os
import fitz
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Hugging Face token and headers
TOKEN = os.getenv("HF_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# Get model URL based on task type
def get_model_url(task_type):
    if task_type in ["code_generation", "bug_fix"]:
        #return "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
        return "https://api-inference.huggingface.co/models/bigscience/bloom-560m"
    else:
        #return "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
        return "https://api-inference.huggingface.co/models/bigscience/bloom-560m"

# Extract text from uploaded PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    content = ""
    for page in doc:
        content += page.get_text()
    return content

# Ask AI to classify or generate text
def ask_ai(prompt_text, task_type="requirements"):
    model_url = get_model_url(task_type)

    try:
        response = requests.post(
            model_url,
            headers=HEADERS,
            json={"inputs": prompt_text},
        )

        print("Status Code:", response.status_code)
        print("Raw Response Text:", response.text)

        response.raise_for_status()

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as e:
            print(f"❌ JSON Decode Error: {e}")
            return f"JSON decode error: {e}. Response: {response.text}"

        print("DEBUG RESPONSE:", data)

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif isinstance(data, dict):
            if "generated_text" in data:
                return data["generated_text"]
            elif "choices" in data:
                return data["choices"][0].get("text", "No text found.")
            elif "error" in data:
                return f"Error from API: {data['error']}"
            return f"Unexpected response format: {data}"
        else:
            return f"Unrecognized response structure: {data}"

    except requests.exceptions.RequestException as err:
        print(f"❌ Request failed: {err}")
        return f"Request failed: {err}"

# Generate code from prompt
def generate_code(prompt_text):
    instruction = f"Generate code for the following request:\n\n{prompt_text}"
    model_url = get_model_url("code_generation")

    try:
        response = requests.post(
            model_url,
            headers=HEADERS,
            json={"inputs": instruction},
        )

        print("Status Code:", response.status_code)
        print("Raw Response:", response.text)

        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif isinstance(data, dict) and "generated_text" in data:
            return data["generated_text"]
        else:
            return f"Unexpected response format: {data}"

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except requests.exceptions.JSONDecodeError as e:
        return f"JSON decode error: {e}. Raw response: {response.text}"

# Fix buggy code
def fix_buggy_code(code_snippet):
    instruction = (
        "You are a programming assistant. Fix the bugs in the code below and return the corrected version only:\n\n"
        f"{code_snippet}"
    )
    model_url = get_model_url("bug_fix")

    try:
        response = requests.post(
            model_url,
            headers=HEADERS,
            json={"inputs": instruction},
        )

        print("Status Code:", response.status_code)
        print("Raw Response Text:", response.text)

        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif isinstance(data, dict):
            if "generated_text" in data:
                return data["generated_text"]
            elif "error" in data:
                return f"Error from API: {data['error']}"
            else:
                return f"Unexpected response format: {data}"
        else:
            return "Something went wrong with the AI response."

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except requests.exceptions.JSONDecodeError as e:
        return f"JSON decode error: {e}. Raw response: {response.text}"

# Generate unittest test cases
def generate_test_cases(code_snippet):
    prompt = (
        "You are a test engineer. Generate Python unittest test cases for the following code:\n\n"
        f"{code_snippet}\n\n"
        "Provide only the test code in unittest format."
    )

    model_url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

    try:
        response = requests.post(
            model_url,
            headers=HEADERS,
            json={"inputs": prompt},
        )

        response.raise_for_status()

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as json_err:
            print("❌ JSON decode error:", json_err)
            print("⚠️ Response content was not JSON:\n", response.text)
            return "Failed to decode AI response."

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]

        print("⚠️ Unexpected JSON structure:", data)
        return "Unexpected response format."

    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
        return "Request to AI model failed."

# Summarize code logic
def summarize_code(code_snippet):
    prompt = (
        "You are a software documentation assistant. Summarize what the following Python code does:\n\n"
        f"{code_snippet}\n\n"
    )

    model_url = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

    try:
        response = requests.post(
            model_url,
            headers=HEADERS,
            json={"inputs": prompt},
        )

        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]

        return "Unexpected response format."

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except requests.exceptions.JSONDecodeError as e:
        return f"JSON decode error: {e}. Raw response: {response.text}"

# AI Chatbot
def ai_chatbot(user_question):
    prompt = (
        "You are an AI assistant for a software development team. "
        "Answer questions clearly and helpfully. "
        "User asked: " + user_question
    )

    model_url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

    try:
        response = requests.post(
            model_url,
            headers=HEADERS,
            json={"inputs": prompt},

        )

        response.raise_for_status()

        if response.text.strip() == "":
            print("Empty response received.")
            return "Error: Received an empty response from the model."

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError as json_err:
            print("JSON decode error:", json_err)
            print("Response content:", response.text)
            return "Error: Failed to decode the response from the model."

        if isinstance(data, list) and len(data) > 0:
            return data[0].get("generated_text", "No response generated.")
        else:
            print("Unexpected response format:", data)
            return "Error: Unexpected response format from the model."

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred:", http_err)
        return f"HTTP error: {http_err}"
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the server. Check your internet connection."
    except requests.exceptions.Timeout:
        return "Error: The request timed out."
    except requests.exceptions.RequestException as req_err:
        print("Request exception:", req_err)
        return f"Error: An error occurred during the request."

# Test chatbot directly
if __name__ == "__main__":
    print(ai_chatbot("What is software testing?"))
