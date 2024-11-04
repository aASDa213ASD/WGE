class Joycon:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.min_limit: int = -32768
        self.max_limit: int = 32767

    def is_valid_axis(self, axis: str) -> bool:
        if axis not in ['x', 'y']:
            return False
        return True

    def clamp(self, value):
        return max(self.min_limit, min(self.max_limit, value))
    
    def reset(self):
        self.x = 0
        self.y = 0
