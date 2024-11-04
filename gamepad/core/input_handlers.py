from pynput import mouse, keyboard


class MouseHandler:
    def __init__(self, controller):
        self.controller = controller
        self.listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click
        )
    
    def on_move(self, x, y):
        self.controller.process_mouse_movement(x, y)

    def on_click(self, x, y, button, pressed):
        self.controller.process_mouse_click(x, y, button, pressed)
    
    def start(self):
        self.listener.start()


class KeyboardHandler:
    def __init__(self, controller):
        self.controller = controller
        self.listener = keyboard.Listener(
            on_press=lambda key: self.on_key(key, True),
            on_release=lambda key: self.on_key(key, False)
        )
    
    def on_key(self, key, pressed):
        self.controller.process_key_event(key, pressed)

    def start(self):
        self.listener.start()
