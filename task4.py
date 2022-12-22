#Напишите программу, которая принимает на вход два числа.
#Получите значение N, для пустого списка, заполните числами в диапазоне [-N, N].
#Найдите произведение на указазных позициях
n =int(input('введите N '))
#fpos = int(input('введите позицию первого элемента '))
#spos = int(input('введите позицию второго элемента '))
arr1 = []
data = open('H:/обучение/Python/семинары/Pylang_sem2_prog/file.txt', 'r')
for line in data:
    arr1.append(int(line))
data.close()
print(arr1)
m = 1
array = []
for i in range(-n, n+1):
        array.append(i)
for i in range(len(arr1)):
    if 0 < arr1[i] < len(array):
        m *= array[arr1[i]-1]
    else:
        print('Нет таких элементов с такими индексами')
print(array, m)