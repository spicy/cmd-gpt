import openai
from config.settings import OPENAI_API_KEY, CHATGPT_MODEL, CHATGPT_MAX_TOKENS
from services.interfaces import IResponseService

class ChatGPTService(IResponseService):
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = CHATGPT_MODEL
        self.max_tokens = CHATGPT_MAX_TOKENS
        self.conversation_history = []

    def get_response(self, prompt: str) -> str:
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
        self.conversation_history = []