
import random
number = random.randint(-10000, 10000)

lastDigit = abs(number) % 10
if lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastDigit} and is 0")
