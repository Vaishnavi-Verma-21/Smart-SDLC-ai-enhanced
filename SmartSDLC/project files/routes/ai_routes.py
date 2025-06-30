from fastapi import APIRouter, Form
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from services.ai_services import summarize_code_service 

router = APIRouter(prefix="/ai", tags=["AI Tools"])

# Load Hugging Face CodeT5 model once when the server starts
model_name="Salesforce/codet5-base-multi-sum"
tokenizer = AutoTokenizer.from_pretrained(model_name,use_fast=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@router.post("/summarize")
async def summarize_code(code: str = Form(...)):
    # Encode the input code
     
    input_text = "summarize: " + code  #
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate summary
    summary_ids = model.generate(
        input_ids,
        max_length=64,
        num_beams=4,
        early_stopping=True
    )

    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    summary = summarize_code_service(code) 

    return {"summary": summary}
