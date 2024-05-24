from abc import ABC, abstractmethod

class ImageCapture(ABC):
    @abstractmethod
    def capture(self):
        pass