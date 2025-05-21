from karel.stanfordkarel import *

def main():
    """
    Places 10 beepers in the spot that Karel is standing.
    """
    step_one()
    step_two()
    step_one()
    #step_two()
    final()
    super_final()

def step_one():
    for i in range(3):
        put_beeper()
        move()
    turn_left()

def step_two():
    put_beeper()
    move()
    turn_left()

def final():
    put_beeper()
    for i in range(2):
        turn_left()

def super_final():
    move()
    for i in range(3):
        turn_left()
    put_beeper()
    move()
    put_beeper()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()