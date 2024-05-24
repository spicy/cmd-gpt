import os
import platform
import subprocess
from services.interfaces import IOCRService, IResponseService
from core.interfaces import ICaptureService, IChunkService, IDisplayService

class Processor:
    def __init__(self, capture_service: ICaptureService, chunk_service: IChunkService, display_service: IDisplayService, ocr_service: IOCRService, response_service: IResponseService):
        self.capture_service = capture_service
        self.chunk_service = chunk_service
        self.display_service = display_service
        self.ocr_service = ocr_service
        self.response_service = response_service

    def capture_and_process(self):
        try:
            print(f"Capturing image using {self.capture_service.capture_method.__class__.__name__} method...")
            image_path = self.capture_service.capture_image()
            print("Image captured. Performing OCR...")

            extracted_text = self.ocr_service.extract_text(image_path)
            print("Getting response...")
            response = self.response_service.get_response(f"Answer the following questions based on the text. Think step by step: \n{extracted_text}")

            chunks, labels = self.chunk_service.chunk_content(response)
            self.display_service.update_chunks(chunks, labels)
            self.display_service.display_chunk()

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self._remove_image(image_path)

    def _remove_image(self, image_path):
        if os.path.exists(image_path):
            os.remove(image_path)

    def next_chunk(self):
        self.display_service.next_chunk()

    def prev_chunk(self):
        self.display_service.prev_chunk()

    def reply(self):
        try:
            reply = input("(Currently Requires Focus) Enter your reply: ")
            print("Getting response...")
            response = self.response_service.get_response(reply)

            response_chunks, response_labels = self.chunk_service.chunk_content(response, label="Response")
            self.display_service.insert_reply_chunks(response_chunks, response_labels)
            self.display_service.display_chunk()

        except Exception as e:
            print(f"An error occurred while asking a question: {e}")

    def reset_conversation(self):
        self.response_service.reset_conversation()
        print("Conversation history reset.")

    def quit_program(self):
        try:
            if platform.system() == "Windows":
                subprocess.run("taskkill /F /IM cmd.exe", shell=True)
        except Exception as e:
            print(f"An error occurred while trying to quit the program: {e}")
        finally:
            os._exit(0)