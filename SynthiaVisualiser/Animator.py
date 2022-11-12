class Animator:
    def __init__(self) -> None:
        
        self.a = 255
        self.b = 0.9
        
        pass

    def get_value_eq01(self, x):
        return self.a * self.b**x 