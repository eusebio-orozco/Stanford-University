#!/usr/bin/python3

"""
Eusebio de Jesus Gutierrez Orozco

Convercion de Fahrenheit a Celsius

"""

def main():
    print("Convercion de Fahrenheit a Celsius")
    grados_fahrenheit = input("Introduce la temperatura en grados Fahrenheit: ")
    grados_fahrenheit = float(grados_fahrenheit)
    grados_celsius = (grados_fahrenheit - 32) * 5.0/9.0

    print("Temperatura: " + str(grados_fahrenheit) + "F = " + str(grados_celsius) + "C") 
    

if __name__ == '__main__':
    main()
