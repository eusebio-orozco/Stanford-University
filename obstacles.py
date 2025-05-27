"""
Eusebio de Jesus Gutierrez Orozco
"""
from karel.stanfordkarel import *

def main():
    step_one()

def step_one():
    if front_is_clear():
        move()
        turn_left()
        move()
        step_two()
        step_tres()
        beeper()
        bread()
        move()
        step_tres()
        beeper()
        bread()
        move()
        step_tres()
        grape()

def step_two():
    for i in range(3):
        turn_left()
    move()

def step_tres():       #movimiento principal 1
    for i in range(3):
        turn_left()
    move()

def beeper():          #movimiento principal 2
    put_beeper()
    for i in range(2):
        turn_left()
    move()

def bread():           #movimiento principal 3
    for i in range(3):
        turn_left()

def grape():
    put_beeper()
    turn_left()
    while front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()