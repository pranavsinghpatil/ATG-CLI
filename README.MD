# Local CLI Chatbot

This project is a simple, local command-line interface (CLI) chatbot powered by a Hugging Face transformer model. It maintains a short-term memory of the conversation to provide more contextually relevant responses.

## Features

- **Local Inference:** Runs entirely on your local machine. No API keys required.
- **Chat Memory:** Remembers the last few turns of the conversation.
- **Extensible:** Easily swap out the model by changing the model name in `src/model_loader.py`.
- **Simple CLI:** A clean and simple command-line interface using the `rich` library.

## Getting Started

### Prerequisites

- Python 3.7+

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Chatbot

To start the chatbot, run the following command:

```bash
python main.py
```

You can then start chatting with the bot. To exit, type `/exit`.

## How it Works

-   **`main.py`**: The entry point of the application. It calls the `run_chatbot` function from the interface.
-   **`src/interface.py`**: Creates the CLI using the `rich` library and handles the main chat loop.
-   **`src/model_loader.py`**: Loads a pre-trained language model from Hugging Face Transformers. By default, it uses `distilgpt2`.
-   **`src/chat_memory.py`**: A simple class to store and retrieve the recent history of the conversation.
-   **`tests/test_memory.py`**: Contains unit tests for the chat memory.

## Customization

You can easily change the model used by the chatbot by modifying the `model_name` in `src/model_loader.py`. For example, to use a different model from the Hugging Face Hub, simply change the `model_name` variable:

```python
# in src/model_loader.py
def load_model(model_name: str = "EleutherAI/gpt-neo-125M", ...):
    # ...
```
