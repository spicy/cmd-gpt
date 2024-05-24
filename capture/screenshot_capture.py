from PIL import ImageGrab
from capture.base_image_capture import BaseImageCapture
from config.settings import SCREENSHOT_PATH

class ScreenshotCapture(BaseImageCapture):
    def capture(self):
        screenshot = ImageGrab.grab()
        screenshot.save(SCREENSHOT_PATH)
        return SCREENSHOT_PATH