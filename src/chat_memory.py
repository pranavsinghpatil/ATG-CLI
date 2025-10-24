from collections import deque

class ChatMemory:
    def __init__(self, window_size: int = 5):
        self.window_size = window_size
        self.memory = deque(maxlen=window_size)

    def update(self, user_input: str, bot_reply: str):
        """Add new conversation turn to memory."""
        self.memory.append(f"User: {user_input}\nBot: {bot_reply}")

    def get_context(self):
        """Return formatted context for next generation."""
        return "\n".join(self.memory)

    def clear(self):
        """Clear the conversation history."""
        self.memory.clear()
