# src/interface.py
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
import threading
import time
import re
from src.model_loader import load_model
from src.chat_memory import ChatMemory
from rich.console import Console

console = Console()

def run_chatbot():
    console.print("\n\n[bold cyan]\t\t\t\tWeRo-CLI Chatbot Initialized! Type /exit to quit.[/bold cyan]\n")

    generator = [None]

    def load_model_thread():
        generator[0] = load_model()

    model_thread = threading.Thread(target=load_model_thread)
    model_thread.start()

    with console.status("[bold green]Loading model...[/bold green]", spinner="moon") as status:
        model_thread.join()

    memory = ChatMemory(window_size=3)

    while True:
        user_input = console.input("[bold green]You:[/bold green] ").strip()
        if user_input.lower() in ["/exit", "exit", "quit"]:
            console.print("[bold red]Exiting chatbot. Goodbye! 👋[/bold red]")
            break

        context = memory.get_context()
        prompt = f"System: You are a helpful and friendly chatbot. Please provide a detailed answer of 1-2 sentences.\n{context}\nUser: {user_input}\nBot:"
        
        generated = generator[0](prompt)

        # Improved parsing with regex
        parts = re.split(r'Bot:', generated)
        if len(parts) > 1:
            bot_reply = parts[-1].strip()
            bot_reply = re.split(r'User:', bot_reply)[0].strip()
        else:
            bot_reply = generated[len(prompt):].strip()

        memory.update(user_input, bot_reply)

        # Typing animation (word by word)
        console.print(f"[bold blue]Bot:[/bold blue] ", end="")
        for word in bot_reply.split():
            console.print(word + " ", end="")
            time.sleep(0.1)
        console.print()
