import os
from core.interfaces import IDisplayService

class DisplayService(IDisplayService):
    def __init__(self, hotkeys):
        self.hotkeys = hotkeys
        self.current_chunk_index = 0
        self.chunks = []
        self.chunk_labels = []

    def update_chunks(self, chunks, labels):
        self.chunks = chunks
        self.chunk_labels = labels
        self.current_chunk_index = 0

    def insert_reply_chunks(self, reply_chunks, reply_labels):
        insert_position = self.current_chunk_index + 1
        self.chunks = self.chunks[:insert_position] + reply_chunks + self.chunks[insert_position:]
        self.chunk_labels = self.chunk_labels[:insert_position] + reply_labels + self.chunk_labels[insert_position:]
        self.current_chunk_index = insert_position  # Focus on the first reply chunk

    def display_chunk(self):
        if self.chunks:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Chunk {self.current_chunk_index + 1} of {len(self.chunks)} ({self.chunk_labels[self.current_chunk_index]})\n")
            print(self.chunks[self.current_chunk_index])
            print(f"\n- - - Press '{self.hotkeys['next_chunk']}' for next chunk, '{self.hotkeys['prev_chunk']}' for previous chunk, '{self.hotkeys['capture']}' to start a new capture, '{self.hotkeys['reply']}' to reply to the current capture, or '{self.hotkeys['reset_conversation']}' to reset conversation.")
            print(f"\n- - - Press '{self.hotkeys['quit']}' to quit the program immediately.")

    def next_chunk(self):
        if self.current_chunk_index < len(self.chunks) - 1:
            self.current_chunk_index += 1
            self.display_chunk()

    def prev_chunk(self):
        if self.current_chunk_index > 0:
            self.current_chunk_index -= 1
            self.display_chunk()