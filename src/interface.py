# src/interface.py
import threading
from src.model_loader import load_model
from src.chat_memory import ChatMemory
from rich.console import Console

console = Console()

def run_chatbot():
    console.print("[bold cyan]🤖 Local CLI Chatbot Initialized! Type /exit to quit.[/bold cyan]\n")

    generator = [None]  # Use a list to hold the generator so it can be modified by the thread

    def load_model_thread():
        generator[0] = load_model()

    model_thread = threading.Thread(target=load_model_thread)
    model_thread.start()

    with console.status("[bold green]Loading model...[/bold green]", spinner="dots") as status:
        model_thread.join()

    memory = ChatMemory(window_size=3)

    while True:
        user_input = console.input("[bold green]You:[/bold green] ").strip()
        if user_input.lower() in ["/exit", "exit", "quit"]:
            console.print("[bold red]Exiting chatbot. Goodbye! 👋[/bold red]")
            break

        context = memory.get_context()
        prompt = f"{context}\nUser: {user_input}\nBot:"
        generated = generator[0](prompt)

        # Extract only new bot text (ignore repeated context)
        bot_reply = generated.split("Bot:")[-1].strip().split("User:")[0]
        memory.update(user_input, bot_reply)

        console.print(f"[bold blue]Bot:[/bold blue] {bot_reply}\n")

