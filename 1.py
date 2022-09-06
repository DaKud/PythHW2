# Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# 1 var # print(sum([int(i) for i in list(str(int(input('a='))))]))

#2 var
num = float(input('Insert number: '))
def numbers_sum(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(f"Sum of numbers = {numbers_sum(num)}")