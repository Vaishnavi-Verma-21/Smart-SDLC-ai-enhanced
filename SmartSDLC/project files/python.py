import requests

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {
    "Authorization": "Bearer hf_your_token"
}
def query(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    response.raise_for_status()
    return response.json()

prompt = "'''Write a Python function that checks if a string is a palindrome.'''\n"
try:
    output = query(prompt)
    print("Model output:\n", output[0]["generated_text"])
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
