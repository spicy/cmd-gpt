from config.settings import HOTKEYS
from core.processor import Processor
from services.ocr_service import OCRService
from services.chatgpt_service import ChatGPTService
from utils.hotkeys import HotkeyManager

def main():
    ocr_service = OCRService()
    chatgpt_service = ChatGPTService()
    processor = Processor(ocr_service, chatgpt_service, HOTKEYS)
    hotkey_manager = HotkeyManager(HOTKEYS, processor)
    hotkey_manager.setup_hotkeys()

if __name__ == "__main__":
    main()