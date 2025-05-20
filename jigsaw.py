from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    """
    The objective is to partition Karel's movement into three distinct 
    sections, each implemented as a separate `def` function
    """
    first()
    second()
    third()
    finish()

    """
    This is the first section of the movement.
    """
def first():
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    
    """
    In this second section, karel move
    """
def second():
    move()
    turn_left()
    turn_left()

    """
    In this third section, Karel places the figure.
    """

def third():
    put_beeper()
    move()
    move()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    move()
    move()
    turn_left()

def finish():
    move()
    turn_left()









# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()