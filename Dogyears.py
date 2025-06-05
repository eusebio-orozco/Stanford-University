# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
     edad_age = input("Enter an age in calendar years: ")
     edad_age = float(edad_age)
     #total = edad_age * DOG_YEARS_MULTIPLIER
     print("That's" + str(edad_age * DOG_YEARS_MULTIPLIER) + "in dog years!" )


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()