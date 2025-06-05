"""
Eusebio de Jesus Gutierrez Orozco

Convercion de Fahrenheit a Celsius

"""

def main():
    #print("Convercion de Fahrenheit a Celsius")
    grados_fahrenheit = input("Enter temperature in Fahrenheit: ")
    grados_fahrenheit = float(grados_fahrenheit)
    grados_celsius = (grados_fahrenheit - 32) * 5.0/9.0

    print("Temperature: " + str(grados_fahrenheit) + "F = " + str(grados_celsius) + "C") 
    

if __name__ == '__main__':
    main()