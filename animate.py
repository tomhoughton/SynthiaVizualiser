class Animate:
    def __init__(self,  anim_type):
        
        """
        The purpose of this class is to take care of all of the animations
        This contains various functions and methods to change values over time, 
        as well as includes the logic to decide which value to feed to the elements.
        """

        self.anim_type = anim_type
        self.current_value = 0

    def anim(self, x):
        # This function will return a new RGB value dependant on whether is is greater or equal to previous.

        # Calculate new value:
        new_val = self.expo_increase(x = x)

        # Compare:
        if new_val > self.current_value:
            self.current_value = new_val
            return int(new_val)
        else:
            decrease = self.current_value - 2
            self.current_value = int(decrease)
            return int(decrease)

    def expo_increase(self, x):
        h = 58.1392623
        c = 0
        b = 1.1

        return (b**(x+h)) + c
    
