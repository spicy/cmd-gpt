import openai
from config import OPENAI_API_KEY, CHATGPT_MODEL, CHATGPT_MAX_TOKENS

class ChatGPT:
    def __init__(self, api_key, model=CHATGPT_MODEL, max_tokens=CHATGPT_MAX_TOKENS):
        openai.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.conversation_history = []

    def get_response(self, prompt):
        self.conversation_history.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *self.conversation_history
            ],
            max_tokens=self.max_tokens
        )

        response_content = response.choices[0].message['content'].strip()
        self.conversation_history.append({"role": "assistant", "content": response_content})
        return response_content

    def reset_conversation(self):
        """Resets the conversation history."""
        self.conversation_history = []