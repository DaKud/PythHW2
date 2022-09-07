# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.

number = int(input('Insert number:' ))
result = list()

sum = 0
for i in range(1, number+1):
    sum = int(sum + round((1+1/i) ** i, 0))
    result.append(sum)
print(f'n = {number} and as  result you will get {list(enumerate(result,))}')