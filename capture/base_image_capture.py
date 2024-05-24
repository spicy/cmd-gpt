from abc import ABC, abstractmethod

class BaseImageCapture(ABC):
    @abstractmethod
    def capture(self):
        pass