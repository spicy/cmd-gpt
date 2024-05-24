import cv2
from capture.base_capture import ImageCapture
from config import CAMERA_IMAGE_PATH

class CameraCapture(ImageCapture):
    def capture(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Cannot open camera")
        ret, frame = cap.read()
        cap.release()
        if not ret:
            raise RuntimeError("Failed to capture image")
        cv2.imwrite(CAMERA_IMAGE_PATH, frame)
        return CAMERA_IMAGE_PATH