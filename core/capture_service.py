from config.settings import CAPTURE_METHOD
from capture.screenshot_capture import ScreenshotCapture
from capture.camera_capture import CameraCapture
from core.interfaces import ICaptureService

class CaptureService(ICaptureService):
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