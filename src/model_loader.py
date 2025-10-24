
from transformers import T5ForConditionalGeneration, T5Tokenizer

def load_model(model_name: str = "google/flan-t5-large"):
    """
    T5 model and tokenizer.
    """
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    
    def chat_fn(prompt):
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        outputs = model.generate(
            input_ids,
            max_new_tokens=100,
            min_length=20,
            repetition_penalty=2.0,
            no_repeat_ngram_size=2,
        )
        return tokenizer.decode(outputs[0], skip_special_tokens=True)

    return chat_fn
