from PIL import ImageGrab
from capture.base_capture import ImageCapture
from config.settings import SCREENSHOT_PATH

class ScreenshotCapture(ImageCapture):
    def capture(self):
        screenshot = ImageGrab.grab()
        screenshot.save(SCREENSHOT_PATH)
        return SCREENSHOT_PATH