import pytesseract
from PIL import Image

class OCR:
    @staticmethod
    def extract_text(image_path):
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        return pytesseract.image_to_string(Image.open(image_path))