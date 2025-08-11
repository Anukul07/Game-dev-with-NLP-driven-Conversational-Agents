import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_DIR = os.path.join(os.path.dirname(__file__), '../../saved_models/distilgpt2-finetuned')

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
print(f"Model loaded on device: {device}")

STOP_TOKENS = ["<END>"]  

def _trim_to_stop(text: str) -> str:
    
    for stop in STOP_TOKENS:
        idx = text.find(stop)
        if idx != -1:
            return text[:idx].strip()

    nl = text.find("\n")
    return text[:nl].strip() if nl != -1 else text.strip()

def generate_npc_reply(
    prompt: str,
    max_new_tokens: int = 80,
    temperature: float = 0.7,
    top_k: int = 50,
    top_p: float = 0.95,
    repetition_penalty: float = 1.15,
) -> str:
    try:
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

        output_ids = model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repetition_penalty=repetition_penalty,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
        )

    
        new_tokens = output_ids[0, input_ids.size(-1):]
        gen_text = tokenizer.decode(new_tokens, skip_special_tokens=False).strip()

        return _trim_to_stop(gen_text)
    except Exception as e:
        print(f"[ERROR in generate_npc_reply]: {e}")
        return "…(falls silent)"

