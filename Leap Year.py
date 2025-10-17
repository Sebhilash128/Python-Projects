print("     -- Leap Year Checker ---")

#Method one:

Year=int(input("Enter a year to check if it is a leap year: "))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(f"{Year} is a leap year.")
else:
    print(f"{Year} is not a leap year.")

#Method two:

for i in range(1):
    Year=int(input("Enter a year to check if it is a leap year: "))

    if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
        print(f"{Year} is a leap year.")
    else:
        print(f"{Year} is not a leap year.")

#Method three:

while True:
    Year=int(input("Enter a year to check if it is a leap year (or type 0 to exit): "))

    if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
        print(f"{Year} is a leap year.")
        break
    else:
        print(f"{Year} is not a leap year.")






