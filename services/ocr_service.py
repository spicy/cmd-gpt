import pytesseract
from PIL import Image
from services.interfaces import IOCRService

class OCRService(IOCRService):
    def extract_text(self, image_path: str) -> str:
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        return pytesseract.image_to_string(Image.open(image_path))