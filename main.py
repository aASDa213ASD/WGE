from gamepad.core.controller import Controller
from time import sleep


def get_launch_message() -> str:
    return """
Windows Gamepad Emulator (WGE) made by @aASDa213ASD
Project github link: https://github.com/aASDa213ASD/WGE
    """

if __name__ == '__main__':
    print(get_launch_message())
    gamepad = Controller()
    gamepad.launch_heartbeat()
