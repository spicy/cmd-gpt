import keyboard

class HotkeyManager:
    def __init__(self, hotkeys, processor):
        self.hotkeys = hotkeys
        self.processor = processor

    def setup_hotkeys(self):
        keyboard.add_hotkey(self.hotkeys['capture'], self.processor.capture_and_process)
        keyboard.add_hotkey(self.hotkeys['next_chunk'], self.processor.next_chunk)
        keyboard.add_hotkey(self.hotkeys['prev_chunk'], self.processor.prev_chunk)
        keyboard.add_hotkey(self.hotkeys['reply'], self.processor.reply)
        keyboard.add_hotkey(self.hotkeys['reset_conversation'], self.processor.reset_conversation)
        keyboard.add_hotkey(self.hotkeys['quit'], self.processor.quit_program)

        print(f"\n- - - Press '{self.hotkeys['capture']}' to start a new capture.")
        keyboard.wait()