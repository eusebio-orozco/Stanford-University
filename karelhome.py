from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    first_step()
    turn_right()
    second_step()
    final_step()

def first_step():
    move()
    move()
    
def turn_right():    
    turn_left()
    turn_left()
    turn_left()

def second_step():
    move()
    turn_left()
    move()
    pick_beeper()

def final_step():
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()