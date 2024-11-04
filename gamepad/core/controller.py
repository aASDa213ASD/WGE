from ..joycons.left import LeftJoycon
from ..joycons.right import RightJoycon
from .input_handlers import KeyboardHandler, MouseHandler
from .devices import get_device
from winapi.winapi import WindowsAPI
from common.settings import (
    GENERAL_KEYBINDS, MOVEMENT_KEYBINDS, 
    MOUSE_KEYBINDS, PAUSE_KEY, HIDE_CURSOR_KEY
)
from vgamepad.win.vigem_commons import XUSB_BUTTON
from threading import Thread
from time import sleep


class Controller:
    def __init__(self):
        self.is_paused = True
        self.left_joycon = LeftJoycon()
        self.right_joycon = RightJoycon()
        self.mouse = MouseHandler(self)
        self.keyboard = KeyboardHandler(self)
        self.windows_api = WindowsAPI()
        self.device = get_device()

    def launch_heartbeat(self):
        self.__hook_peripherals()

        try:
            print('\nJumping into heartbeat infinite loop.')
            while (True):
                sleep(10)
        except KeyboardInterrupt:
            # Forcefully show cursor if it was hidden on exit
            self.windows_api.show_cursor()
            # Disconnect from ViGemBus by activating garbage collector
            del self.device

    def toggle_pause(self):
        self.is_paused = not self.is_paused
    
    def process_mouse_movement(self, x, y):
        if self.is_paused:
            return
        
        self.right_joycon.set_position(x, y)
        self.device.right_joystick(
            self.right_joycon.x,
            self.right_joycon.y
        )
        self.device.update()
    
    def process_mouse_click(self, x: int, y: int, button, pressed: bool):
        if self.is_paused:
            return
        
        button_name: str = button.name
        action: str = MOUSE_KEYBINDS.get(button_name)

        if not action:
            return
    
        if isinstance(action, XUSB_BUTTON):
            if pressed:
                self.device.press_button(button=action)
            else:
                self.device.release_button(button=action)
        elif hasattr(self.device, action):
            method = getattr(self.device, action)
            if callable(method):
                method(255 if pressed else 0)
        elif action == 'calibrate':
            self.right_joycon.calibrate(x, y)
            
        self.device.update()
    
    def process_key_event(self, key, pressed):
        key_name = self._get_key_name(key)

        if self._handle_special_keys(key_name, pressed):
            return

        if self.is_paused:
            return

        if self._process_movement_keybind(key_name, pressed):
            self.device.left_joystick(self.left_joycon.x, self.left_joycon.y)
        else:
            self._process_general_keybind(key_name, pressed)

        self.device.update()

    def _get_key_name(self, key) -> str:
        """Extract and return the key name as a lowercase string."""
        try:
            return str(key.char).lower()
        except AttributeError:
            return str(key.name).lower()

    def _handle_special_keys(self, key_name: str, pressed: bool) -> bool:
        """Handle pause and cursor visibility keys. Return True if handled."""
        if key_name == PAUSE_KEY and pressed:
            self.toggle_pause()
            return True

        if key_name == HIDE_CURSOR_KEY and pressed:
            self.windows_api.switch_cursor_visibility()
            return True

        return False

    def _process_movement_keybind(self, key_name: str, pressed: bool) -> bool:
        """Process movement keybinds if found, return True if action taken."""
        action = MOVEMENT_KEYBINDS.get(key_name)
        if not action:
            return False

        method = getattr(self.left_joycon, action['method'], None)
        if callable(method):
            if action['method'] == 'set_axis':
                method(action['axis'], action['value'] if pressed else 0)
            elif action['method'] == 'switch_half_mode' and pressed:
                method()

        return True

    def _process_general_keybind(self, key_name: str, pressed: bool):
        """Send input for general keybinds."""
        action = GENERAL_KEYBINDS.get(key_name)
        if action:
            self.__send_input(button=action, pressed=pressed)


    def __send_input(self, button, pressed):
        if pressed:
            self.device.press_button(button=button)
        else:
            self.device.release_button(button=button)
    
    def __hook_peripherals(self):
        print('Invoking a mouse listener ... ', end='')
        Thread(target=self.mouse.start).start()
        print('OK')

        print('Invoking a keyboard listener ... ', end='')
        Thread(target=self.keyboard.start).start()
        print('OK')