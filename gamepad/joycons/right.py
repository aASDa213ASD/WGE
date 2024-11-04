from .base import Joycon
from common.settings import JOYCON_RIGHT_SENSITIVITY

class RightJoycon(Joycon):
    def __init__(self):
        super().__init__()
        self.sensitivity: int = JOYCON_RIGHT_SENSITIVITY
        self.origin_x: int = 0
        self.origin_y: int = 0

    def set_position(self, x: int, y: int):
        self.x = self.clamp((x - self.origin_x) * self.sensitivity)
        self.y = self.clamp((y - self.origin_y) * -self.sensitivity)

    def calibrate(self, x, y):
        self.origin_x, self.origin_y = x, y
        self.reset()
