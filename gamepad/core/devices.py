# ViGemBus device initializator
import vgamepad as vg


def get_device():
    print('Connecting to ViGemBus client ... ', end='')
    device: vg.VX360Gamepad = vg.VX360Gamepad()
    print('OK' if isinstance(device, vg.VX360Gamepad) else 'ERROR')
    return device