# services/ai_chat_service.py

#from langchain.llms import HuggingFacePipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_huggingface import HuggingFacePipeline


from transformers import pipeline

# Load a basic Hugging Face model like GPT-2
hf_pipeline = pipeline("text-generation", model="gpt2", max_length=100)
llm = HuggingFacePipeline(pipeline=hf_pipeline)

def generate_response(prompt: str) -> str:
    response = llm(prompt)
    return response
