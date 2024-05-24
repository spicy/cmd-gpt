# HiddenGPT

HiddenGPT is a Python terminal application designed to capture images using screenshots or a camera, perform Optical Character Recognition (OCR) on the captured images, and interact with GPT models (like GPT4o from OpenAI) to provide responses based on the extracted text. The application is modular and follows principles for maintainability and scalability.

## Features

- Capture images using screenshots or a camera.
- Perform OCR on captured images to extract text.
- Interact with GPT models to get responses based on the extracted text.
- Display responses in manageable chunks.
- Navigate through text chunks using keyboard hotkeys even when the terminal is not focused.
- Ask text follow-up questions on the responses received.

## Folder Structure

```text
HiddenGPT/
│
├── capture/
│   ├── base_capture.py         - Defines the abstract base class for image capture methods.
│   ├── camera_capture.py       - Implements the image capture functionality using a camera.
│   ├── screenshot_capture.py   - Implements the image capture functionality using screenshots.
│
├── core/
│   ├── capture_service.py      - Manages the image capture process using the appropriate capture method.
│   ├── chunk_service.py        - Handles the splitting of text content into chunks.
│   ├── display_service.py      - Manages the display and navigation of text chunks.
│   ├── processor.py            - Orchestrates the capture, processing, and display of images and text.
│
├── services/
│   ├── chatgpt_service.py      - Implements interaction with OpenAI's GPT models.
│   ├── ocr_service.py          - Implements OCR functionality to extract text from images.
│   ├── interfaces.py           - Defines interfaces for the OCR and GPT Response services.
│
├── config/
│   ├── settings.py             - Contains configuration settings and environment variables.
│
├── utils/
│   ├── hotkeys.py              - Manages keyboard hotkeys for interacting with the application.
│
├── main.py                     - Entry point for the application, setting up and running the processor and hotkeys.
├── requirements.txt            - Lists the Python dependencies required for the project.
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/spicy/HiddenGPT.git
   cd HiddenGPT
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Or just: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the project root directory and add your OpenAI API key:

   ```env
   HIDDENGPT_OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the application**:

   ```bash
   python main.py
   ```

2. **Default Hotkeys**:
   - `7` : Capture an image and process it.
   - `=` : Display the next chunk of text.
   - `-` : Display the previous chunk of text.
   - `8` : Ask a follow-up question.
   - `F4` : Reset the GPT conversation.
   - `F8` : Quit the application.

## Configuration

The configuration settings are located in `config/settings.py`. Please modify these as desired.

```python
# Configuration settings
SCREENSHOT_PATH = 'screenshot.png'
CAMERA_IMAGE_PATH = 'camera_image.jpg'
CAPTURE_METHOD = 'screenshot' # Options: 'screenshot' or 'camera'
MAX_LINES_PER_CHUNK = 12

# ChatGPT
CHATGPT_MODEL = 'gpt-4o' # Other valid options: 'gpt-4', 'gpt-3.5-turbo', etc.


CHATGPT_MAX_TOKENS = 1000 # 1000 Tokens is ~750 words.

# Hotkeys
HOTKEY_CAPTURE = '7'
HOTKEY_REPLY = '8'
HOTKEY_NEXT_CHUNK = '='
HOTKEY_PREV_CHUNK = '-'
HOTKEY_RESET_CONVERSATION = 'F4'
HOTKEY_QUIT = 'F8'
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [OpenAI](https://www.openai.com/) for powerful GPT models.
- [Pytesseract](https://github.com/madmaze/pytesseract) for OCR capabilities.
- [Keyboard](https://github.com/boppreh/keyboard) for managing keyboard hotkeys while unfocused.
