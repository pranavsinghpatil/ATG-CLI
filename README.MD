# WeRo Command-Line Chatbot using Hugging Face

This project is a fully functional local chatbot interface developed as part of the ATG Technical Assignment for a Machine Learning Intern position. The chatbot uses a Hugging Face text generation model to provide an interactive conversational experience in the command line.

## Demo_video :
demo_video file is there in repo's root dir.

Watch it online ->[https://drive.google.com/file/d/16Jt43CCNp8kJhurXev2Z1897FDaoQ0YO/view?usp=sharing] 

## Task Overview

The main objective of this project is to design and implement a command-line chatbot in Python that uses a Hugging Face-supported text generation model. The chatbot is required to maintain a short-term memory of previous exchanges using a sliding window mechanism to ensure coherent multi-turn conversation.

## Features

-   **Local AI:** Runs entirely on your local machine, so no internet connection or API keys are required after the initial setup.
-   **Conversational Memory:** Remembers the last few turns of the conversation to provide more context-aware responses.
-   **Interactive CLI:** A polished and user-friendly command-line interface with features like:
    -   A placeholder text for the input prompt.
    -   A "typing" animation for the bot's responses.
    -   A clean and organized layout.
-   **Commands:**
    -   `/exit`: Exit the chatbot.
    -   `/reset`: Reset the conversation history.
    -   `/clear`: Clear the terminal screen.

## Getting Started

### Prerequisites

-   Python 3.7+

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/pranavsinghpatil/WeRo-CLI.git
    cd WeRo-CLI
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

## Usage
Note: Dont forget to HF_login in terminal.
To start the chatbot, run the following command in your terminal:

```bash
python main.py
```

You can then start chatting with the bot. Use the commands listed in the command menu to manage the session.

### Sample Interaction

```
You: what is capital of India?
Bot: Delhi, India.
You: where is ponducherry?
Bot: Bottle: Pondicherry is a city in the Indian state of Tamil Nadu.
User: /exit
Exiting chatbot. Goodbye!
```

## Project Structure

The project is organized into the following modular Python scripts:

-   `main.py`: The entry point of the application.
-   `src/interface.py`: Handles the command-line interface, user input, and the main chat loop.
-   `src/model_loader.py`: Responsible for loading the Hugging Face model and tokenizer.
-   `src/chat_memory.py`: Implements the sliding window mechanism for the conversation history.

## Technologies Used

-   **Python:** The core programming language for the project.
-   **Hugging Face Transformers:** The library that provides the pre-trained language model.
    -   **Model:** `google/flan-t5-large` - A powerful text-to-text model that is a good compromise between conversational ability and question-answering.
-   **PyTorch:** The deep learning framework used by the transformer model.
-   **Rich:** A Python library for rich text and beautiful formatting in the terminal.
-   **Prompt Toolkit:** A library for building powerful interactive command-line applications in Python.

## Author

-- by [PranavSingh](https://github.com/pranavsinghpatil)
