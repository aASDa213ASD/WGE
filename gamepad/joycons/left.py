from .base import Joycon


class LeftJoycon(Joycon):
    def __init__(self):
        super().__init__()
        self.half_mode: bool = False

    def set_axis(self, axis: str, value: int):
        if not self.is_valid_axis(axis):
            raise ValueError(f'Unknown axis {axis}, known are: x, y')
        
        if value != 0:
            value = self.clamp(value)
            
            if self.half_mode:
                value //= 2
        
        setattr(self, axis, value)
    
    def switch_half_mode(self):
        self.half_mode = not self.half_mode