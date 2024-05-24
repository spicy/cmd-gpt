import os

# Configuration settings
SCREENSHOT_PATH = 'screenshot.png'
CAMERA_IMAGE_PATH = 'camera_image.jpg'
CAPTURE_METHOD = 'screenshot'

# ChatGPT
OPENAI_API_KEY = os.getenv('HIDDENGPT_OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("No HiddenGPT OpenAI API key found in environment variables")
CHATGPT_MODEL = 'gpt-4o'
CHATGPT_MAX_TOKENS = 1000

# Hotkeys
HOTKEY_CAPTURE = '7'
HOTKEY_REPLY = '8'

HOTKEY_NEXT_CHUNK = '='
HOTKEY_PREV_CHUNK = '-'

HOTKEY_RESET_CONVERSATION = 'F4'
HOTKEY_QUIT = 'F8'

HOTKEYS = {
    'capture': HOTKEY_CAPTURE,
    'reply': HOTKEY_REPLY,
    'next_chunk': HOTKEY_NEXT_CHUNK,
    'prev_chunk': HOTKEY_PREV_CHUNK,
    'reset_conversation': HOTKEY_RESET_CONVERSATION,
    'quit': HOTKEY_QUIT,
}

MAX_LINES_PER_CHUNK = 12