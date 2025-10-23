# src/model_loader.py
from transformers import pipeline

def load_model(model_name: str = "mistralai/Mistral-7B-Instruct-v0.2", max_new_tokens: int = 150, temperature: float = 0.8):
    """
    Load a conversational text generation model.
    """
    print(f"[INFO] Loading model '{model_name}'...")
    generator = pipeline("text-generation", model=model_name, truncation=True)
    print("[INFO] Model loaded successfully ✅")
    
    def chat_fn(prompt):
        outputs = generator(
            prompt,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            do_sample=True,
            pad_token_id=50256
        )
        return outputs[0]["generated_text"]

    return chat_fn
