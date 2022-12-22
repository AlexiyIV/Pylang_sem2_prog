# задайте список из N чисел последовательности (1 + 1/n)^n
n = int(input('Введите количество элементов словаря '))
dict = {i: (1+1/i)**i for i in range(1, n+1)}
sum = 0
for i in range(1, len(dict)+1):
    sum += dict[i]
print(dict)
