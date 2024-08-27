import pytesseract
from PIL import Image
from services.interfaces import IOCRService

class OCRService(IOCRService):
    def extract_text(self, image_path: str) -> str:
        with Image.open(image_path) as img:
            custom_config = r'--oem 3 --psm 6'
            return pytesseract.image_to_string(img, config=custom_config)

    def extract_data(self, image_path: str) -> dict:
        with Image.open(image_path) as img:
            custom_config = r'--oem 3 --psm 6'
            data = pytesseract.image_to_data(img, config=custom_config, output_type=pytesseract.Output.DICT)
            return data