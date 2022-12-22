# Напишите программу, которая на вход получает число N и выдаё1т набор произведений чисел от 1 до N
n = int(input('Введите N '))
array = [1 for i in range(n)]
for i in range(1,len(array)):
    array[i] = array[i-1]*(i+1)
print(array)