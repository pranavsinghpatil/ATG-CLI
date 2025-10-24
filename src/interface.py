# src/interface.py
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
import threading
import time
from src.model_loader import load_model
from src.chat_memory import ChatMemory
from rich.console import Console
from rich.panel import Panel

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML

console = Console()

def run_chatbot():
    generator = [None]

    def load_model_thread():
        generator[0] = load_model()

    model_thread = threading.Thread(target=load_model_thread)
    model_thread.start()

    with console.status("[bold green]Loading model...[/bold green]", spinner="moon") as status:
        model_thread.join()

    os.system('cls')

    console.print("\n[bold cyan]\t\t\t\t\tWeRo-CLI Chatbot Initialized! [/bold cyan] [dim magenta]\t\t\t\t--- [link=https://github.com/pranavsinghpatil]PranavSingh[/link][/dim magenta]\n")
    # console.print("\n")

    command_panel = Panel(
        "[dim cyan]/exit[/dim cyan] - Exit the chatbot\n"
        "[dim cyan]/reset[/dim cyan] - Reset the conversation history\n"
        "[dim cyan]/clear[/dim cyan] - Clear the screen",
        title="[bold]Commands[/bold]",
        border_style="dim",
        expand=False
    )
    console.print(command_panel)

    memory = ChatMemory(window_size=3)

    while True:
        user_input = prompt(HTML('<style fg="green">You:</style> '), placeholder=HTML('<style fg="gray">write message</style>')).strip()
        
        if user_input.lower() in ["/exit", "exit", "quit"]:
            console.print("[bold red]Exiting chatbot. Goodbye! 👋[/bold red]")
            break
        
        if user_input.lower() == "/reset":
            memory.clear()
            console.print("[bold yellow]Conversation history has been reset.[/bold yellow]")
            continue

        if user_input.lower() == "/clear":
            os.system('cls')
            console.print("\n[bold magenta]\t\t\tWeRo-CLI Chatbot Initialized! Type /exit to quit.[/bold magenta]\n")
            console.print("[cyan]\t\t\t\t\t\t\t\t--- [link=https://github.com/pranavsinghpatil]PranavSingh[/link][/cyan]\n")
            console.print(command_panel)
            continue



        context = memory.get_context()
        prompt_for_model = f"answer the question: {context}\n{user_input}"
        
        bot_reply = generator[0](prompt_for_model)

        memory.update(user_input, bot_reply)

        # Typing animation (word by word)
        console.print(f"[bold blue]Bot:[/bold blue] ", end="")
        for word in bot_reply.split():
            console.print(word + " ", end="")
            time.sleep(0.1)
        console.print()
