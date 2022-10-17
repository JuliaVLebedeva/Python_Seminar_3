# Задача №2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
some_list = []
i = 1
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    some_list.append(randint(1,5))
    i += 1
print(f'Ваш случайно сгенерированный список из {n} элементов: {some_list}')
k=0
j=1
if n%2==0:
    while k<len(some_list)//2:
        mult=some_list[k]*some_list[len(some_list)-j]
        print(mult)
        k+=1
        j+=1
else:
    while k<len(some_list)//2:
        mult=some_list[k]*some_list[len(some_list)-j]
        print('Произведения пар чисел списка:')
        print(mult)
        print(some_list[len(some_list)//2]**2)
        k+=1
        j+=1