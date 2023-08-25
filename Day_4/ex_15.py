import random
number = random.randint(0, 1500)
print(number)
digital = input("введи цифру ")
if digital in str(number):
    print("True")
else:
    print("False")