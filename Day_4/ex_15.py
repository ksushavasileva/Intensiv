import random
number = random.randint(0, 1500)
print(number)
flag = False
digital = int(input("введи цифру "))
while number !=0:
    ost = number % 10
    if ost == digital:
        flag = True
    number = number // 10

print(flag)
