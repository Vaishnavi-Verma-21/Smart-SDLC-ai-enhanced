from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer once when service is loaded
model_name = "Salesforce/codet5-base-multi-sum"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_code_service(code: str) -> str:
    input_text = "summarize: " + code
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    summary_ids = model.generate(
        input_ids,
        max_length=64,
        num_beams=4,
        early_stopping=True
    )
    
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
