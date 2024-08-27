from config.settings import HOTKEYS, CUSTOM_PROMPT
from core.processor import Processor
from core.capture_service import CaptureService
from core.chunk_service import ChunkService
from core.display_service import DisplayService
from services.ocr_service import OCRService
from services.chatgpt_service import ChatGPTService
from utils.hotkey_manager import HotkeyManager
from services.interfaces import IResponseService

def main():
    capture_service = CaptureService()
    chunk_service = ChunkService()
    display_service = DisplayService(HOTKEYS)
    ocr_service = OCRService()
    response_service: IResponseService = ChatGPTService()
    processor = Processor(capture_service, chunk_service, display_service, ocr_service, response_service, CUSTOM_PROMPT)
    hotkey_manager = HotkeyManager(HOTKEYS, processor)
    hotkey_manager.setup_hotkeys()

if __name__ == "__main__":
    main()