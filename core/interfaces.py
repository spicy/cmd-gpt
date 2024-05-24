from abc import ABC, abstractmethod

class ICaptureService(ABC):
    @abstractmethod
    def capture_image(self):
        pass

class IChunkService(ABC):
    @abstractmethod
    def chunk_content(self, content, label="Original"):
        pass

class IDisplayService(ABC):
    @abstractmethod
    def update_chunks(self, chunks, labels):
        pass

    @abstractmethod
    def insert_reply_chunks(self, reply_chunks, reply_labels):
        pass

    @abstractmethod
    def display_chunk(self):
        pass

    @abstractmethod
    def next_chunk(self):
        pass

    @abstractmethod
    def prev_chunk(self):
        pass