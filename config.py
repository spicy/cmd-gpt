import os

# Configuration settings
SCREENSHOT_PATH = 'screenshot.png'
CAMERA_IMAGE_PATH = 'camera_image.jpg'
CAPTURE_METHOD = 'screenshot'

# ChatGPT
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API key found in environment variables")
CHATGPT_MODEL = 'gpt-4o'
CHATGPT_MAX_TOKENS = 1000