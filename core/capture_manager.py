from config.settings import CAPTURE_METHOD
from capture import ScreenshotCapture, CameraCapture

class CaptureManager:
    def __init__(self):
        self.capture_method = self._get_capture_method()

    def _get_capture_method(self):
        if CAPTURE_METHOD == 'screenshot':
            return ScreenshotCapture()
        elif CAPTURE_METHOD == 'camera':
            return CameraCapture()
        else:
            raise ValueError("Invalid capture method specified in config.")

    def capture_image(self):
        return self.capture_method.capture()