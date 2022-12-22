#реализуйте алгоритм перемешивания списка
import random
n = int(input('Введите количество элементов '))
array = [i for i in range(n)]
print(array)
x = 0
y = 0
for i in range(len(array)):
    x = array[i]
    y = random.randint(0, n-1)
    array[i] = array[y]
    array[y] = x
print(array)