# Задача №3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт  между максимальным и 
# минимальным значением дробной части элементов.

some_list=[1.1, 1.2, 3.3, 5, 10.4]
print(f'Текущий список {some_list}')
#new_list=[]
new_list=list(map(float, some_list))
second_list=[round(i%1,2) for i in new_list if i%1 != 0]
print(f'Разница между max и min значениями дробной части {round(max(second_list)-min(second_list),2)}')

