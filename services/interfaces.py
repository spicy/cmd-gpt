from abc import ABC, abstractmethod

class IOCRService(ABC):
    @abstractmethod
    def extract_text(self, image_path: str) -> str:
        pass

class IResponseService(ABC):
    @abstractmethod
    def get_response(self, prompt: str) -> str:
        pass

    @abstractmethod
    def reset_conversation(self):
        pass