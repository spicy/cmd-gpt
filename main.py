import os
import keyboard
import platform
import subprocess
from config import OPENAI_API_KEY, CAPTURE_METHOD
from capture import ScreenshotCapture, CameraCapture
from ocr import OCR
from chatgpt import ChatGPT

HOTKEY_CAPTURE = '7'
HOTKEY_ASK_QUESTION = '8'
HOTKEY_NEXT_CHUNK = '='
HOTKEY_PREV_CHUNK = '-'
HOTKEY_RESET_CONVERSATION = 'F4'
HOTKEY_QUIT = 'F8'
CHUNK_SIZE = 12

class CaptureProcessor:
    def __init__(self):
        self.chunks = []
        self.chunk_labels = []
        self.current_chunk_index = 0
        self.ocr = OCR()
        self.chatgpt = ChatGPT(OPENAI_API_KEY)
        self.capture_method = self._get_capture_method()

    def _get_capture_method(self):
        """Return the appropriate capture method based on the configuration."""
        if CAPTURE_METHOD == 'screenshot':
            return ScreenshotCapture()
        elif CAPTURE_METHOD == 'camera':
            return CameraCapture()
        else:
            raise ValueError("Invalid capture method specified in config.")

    def _chunk_content(self, content, label="Original"):
        """Split the content into chunks of specified size and add labels."""
        lines = content.split('\n')
        chunks = ['\n'.join(lines[i:i + CHUNK_SIZE]) for i in range(0, len(lines), CHUNK_SIZE)]
        labels = [label] * len(chunks)
        return chunks, labels

    def _display_chunk(self):
        """Clear the console and display the current chunk of text."""
        if self.chunks:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Chunk {self.current_chunk_index + 1} of {len(self.chunks)} ({self.chunk_labels[self.current_chunk_index]})\n")
            print(self.chunks[self.current_chunk_index])
            print(f"\n- - - Press '{HOTKEY_NEXT_CHUNK}' for next chunk, '{HOTKEY_PREV_CHUNK}' for previous chunk, '{HOTKEY_QUIT}' to quit, '{HOTKEY_ASK_QUESTION}' to ask a question, or '{HOTKEY_RESET_CONVERSATION}' to reset conversation.")

    def _remove_image(self, image_path):
        """Remove the image file if it exists."""
        if os.path.exists(image_path):
            os.remove(image_path)

    def capture_and_process(self):
        """Capture an image, perform OCR, get a response from ChatGPT, and display the response in chunks."""
        try:
            print(f"Capturing image using {CAPTURE_METHOD} method...")
            image_path = self.capture_method.capture()
            print("Image captured. Performing OCR...")

            extracted_text = self.ocr.extract_text(image_path)
            # print(f"Extracted Text:\n{extracted_text}\n")

            print("Getting response from ChatGPT...")
            response = self.chatgpt.get_response(
                f"Answer the following questions based on the text. Think step by step: \n{extracted_text}"
            )

            # Prepare content for chunked display
            chunks, labels = self._chunk_content(response)
            self.chunks = chunks
            self.chunk_labels = labels
            self.current_chunk_index = 0
            self._display_chunk()

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self._remove_image(image_path)

    def next_chunk(self):
        """Display the next chunk of text."""
        if self.current_chunk_index < len(self.chunks) - 1:
            self.current_chunk_index += 1
            self._display_chunk()

    def prev_chunk(self):
        """Display the previous chunk of text."""
        if self.current_chunk_index > 0:
            self.current_chunk_index -= 1
            self._display_chunk()

    def ask_question(self):
        """Prompt the user to enter a question and get a response from ChatGPT."""
        try:
            question = input("Enter your question: ")
            print("Getting response from ChatGPT...")
            response = self.chatgpt.get_response(question)

            # Insert the response into the chunks as a new chunk after the current chunk
            response_chunks, response_labels = self._chunk_content(response, label="Response")
            insert_position = self.current_chunk_index + 1
            self.chunks = self.chunks[:insert_position] + response_chunks + self.chunks[insert_position:]
            self.chunk_labels = self.chunk_labels[:insert_position] + response_labels + self.chunk_labels[insert_position:]

            # Move to the first response chunk
            self.current_chunk_index = insert_position
            self._display_chunk()

        except Exception as e:
            print(f"An error occurred while asking a question: {e}")

    def reset_conversation(self):
        """Reset the conversation history in ChatGPT."""
        self.chatgpt.reset_conversation()
        print("Conversation history reset.")

    def quit_program(self):
        """Quit the program and close the command prompt or terminal window."""
        try:
            if platform.system() == "Windows":
                # Closes the current command prompt window
                subprocess.run("taskkill /F /IM cmd.exe", shell=True)
        except Exception as e:
            print(f"An error occurred while trying to quit the program: {e}")
        finally:
            os._exit(0)

    def setup_hotkeys(self):
        """Setup keyboard hotkeys for capturing and navigating chunks."""
        print(f"- - - Press '{HOTKEY_CAPTURE}' to capture the next image, '{HOTKEY_NEXT_CHUNK}' or '{HOTKEY_PREV_CHUNK}' keys to navigate chunks, '{HOTKEY_ASK_QUESTION}' to ask a question, '{HOTKEY_RESET_CONVERSATION}' to reset conversation, or '{HOTKEY_QUIT}' to quit.")
        keyboard.add_hotkey(HOTKEY_CAPTURE, self.capture_and_process)
        keyboard.add_hotkey(HOTKEY_NEXT_CHUNK, self.next_chunk)
        keyboard.add_hotkey(HOTKEY_PREV_CHUNK, self.prev_chunk)
        keyboard.add_hotkey(HOTKEY_ASK_QUESTION, self.ask_question)
        keyboard.add_hotkey(HOTKEY_RESET_CONVERSATION, self.reset_conversation)
        keyboard.add_hotkey(HOTKEY_QUIT, self.quit_program)
        print("- - - Listening for hotkeys...")
        keyboard.wait()

def main():
    processor = CaptureProcessor()
    processor.setup_hotkeys()

if __name__ == "__main__":
    main()