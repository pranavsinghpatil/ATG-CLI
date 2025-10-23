# src/model_loader.py
from transformers import pipeline

def load_model(model_name: str = "google/flan-t5-base"):
    """
    Load a text-to-text generation model.
    """
    print(f"[INFO] Loading model '{model_name}'...")
    text2text_generator = pipeline("text2text-generation", model=model_name)
    print("[INFO] Model loaded successfully ✅")
    
    def chat_fn(prompt):
        outputs = text2text_generator(
            prompt,
            max_new_tokens=100,
        )
        return outputs[0]["generated_text"]

    return chat_fn
