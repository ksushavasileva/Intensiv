n = int(input())
number_min = 10
while n != 0:
    ost = n % 10
    if ost < number_min:
        number_min = ost
    n = n // 10
print(number_min)
