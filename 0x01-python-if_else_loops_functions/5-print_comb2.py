# program that prints numbers from 0 to 99

for number in range(0, 100):
    if number < 99:
        print(f"{number:02d}", end=", ")
    else:
        print(f"{number:02d}")
