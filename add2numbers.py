#!/usr/bin/python3

"""
Programa: sumar2números
Este programa le pide al usuario dos números enteros y muestra su suma.
"""

def main():
    print("This program adds two numbers.")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    total = num1 + num2
    print("The total is " + str(total) + ".")


if __name__ == '__main__':
    main()
