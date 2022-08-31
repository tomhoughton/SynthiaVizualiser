class Animate:
    def __init__(self,  anim_type):
        
        """
        The purpose of this class is to take care of all of the animations
        This contains various functions and methods to change values over time, 
        as well as includes the logic to decide which value to feed to the elements.
        """

        self.anim_type = anim_type

    def anim(self, x):
        print('anim')

    def expo_increase(self, x):
        h = 58.1392623
        c = 0
        b = 1.1

        return (b**(x+h)) + c
    
