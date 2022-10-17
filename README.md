Семинар 3

Описание видов функций

def summa_numbers(): #эта функця ничего не возвращает, только печатает на экран
    a=3
    b=6
    print(a+b)

#summa1()

def summa2(): #эта функця уже возвращает значение
    a=int(input("Введите первое число "))
    b=int(input("Введите второе число "))
    return a+b

#print(summa2())

x1=6
x2=5

def summa3(): #эта функця уже возвращает значение на основе глобальных переменных - не профессионально
    return x1 + x2

#print(summa3())
sum = 0

def summa4(): #эта функця изменяет глобальную переменную
    global sum
    a=int(input("Введите первое число "))
    b=int(input("Введите второе число "))
    sum = a + b

#summa4()
#print(sum)

def summa5(a,b): #эта функция уже принимает на вход аргументы и возвращает значение
    return a+b

try:
    a1=int(input("Введите первое число "))
    b1=int(input("Введите второе число "))
    print(summa5(a1, b1))
except:
    print("надо было вводить именно целое число")

# 3. Задайте список из n чисел последовательности (1+1/N)**N и 
# выведите на экран их сумму.

def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number

def sequence(n):
    list =[]
    buff = 0
    sum = 0
    for i in range(n):
        buff = (1 + 1/n)**n
        list.append(buff)
        sum += buff
    return sum

n = check_digit('Введите число:')
print(f'Сумма последовательности числа равна: {sequence(n)}')
..............................................................................

def list_posl(number):
list = []
for i in range(1, number + 1):
list.append(round((1 + 1 / i) ** i, 3))
return list

def sum_values_list(list):
sum = 0
for i in list:
sum += i
return sum

try:
num = int(input('Введите целое число: '))

print(f'Последовательность равна: {list_posl(num)}')
print(f'Сумма элементов равна {sum_values_list(list_posl(num))}')


except:
print('Введите целое число.')


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number

m = check_digit('Введите число:')
list1 = []
for i in range(-m, m+1):
        list1.append(i)
print(list1)

path = 'file.txt'
data = open(path, 'r')
proiz = 1
for line in data:
    proiz *= list1[int(line)]
print(proiz)
data.close()

................................................................................
# 20. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

def get_list_from_input(n):
    str_list = [''] * n
    for i in range(n):
        str_list[i] = input(f'Input row {i + 1}: ')

    return str_list


try:
    n = int(input('Input number of rows: '))
except ValueError as ex:
        print('Input natural number!')
        exit(ex)

new_list = get_list_from_input(n)

try:
    num = int(input('Input natural number: '))
except ValueError as ex:
    print('Input natural number!')
    exit(ex)

if str(num) in new_list:
    print(f'Number {num} is found in the list')
else:
    print(f'Number {num} is not found in the list')
.............................
.............................
def get_list_from_input(n):                                       # вытаскиваем строки из файла *тхт.
str_list = [''] * n
for i in range(n):
str_list[i] = input(f'Input row {i + 1}: ')

return str_list


def get_list_from_file(path):
with open(path, 'r') as f:
return f.read().split('\n')


def check_num_in_list(lst, num):
if str(num) in lst:
print(f'Number {num} is found in list')
else:
print(f'Number {num} is not found in list')


try:
n = int(input('Input number of rows: '))
except ValueError as ex:
print('Input natural number!')
exit(ex)

list1 = get_list_from_input(n)

try:
num = int(input('Input natural number: '))
except ValueError as ex:
print('Input natural number!')
exit(ex)

print()
print('List from input: ')
print(list1)
check_num_in_list(list1, num)

path = 'str.txt'
list2 = get_list_from_file(path)

print()
print('List from file: ')
print(list2)
check_num_in_list(list2, num)

...............................................................................................
2. вариант

def create_string_list(number):
list = []
for i in range(number):
list.append(input('Введите что-нибудь: '))
return list

def check_value_in_list(list, number):
for i in list:
if i == number:
print('В списке присутствует ваше число!')

try:
num = input('Введите искомое число: ')
size = int(input('Введите размер списка: '))
list = create_string_list(size)
check_value_in_list(list, num)

except:
print('Некорректный ввод!')



# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def get_list_from_input(n):
    str_list = [''] * n
    for i in range(n):
        str_list[i] = input(f'Input row {i + 1}: ')

    return str_list


def check_string_in_list(l, s):
    count = 0
    for i in range(len(l)):
        if l[i] == s:
            count += 1
        if count == 2:
            return i

    return -1


try:
    n = int(input('Input number of rows: '))
except ValueError as ex:
    print('Input natural number!')
    exit(ex)

new_list = get_list_from_input(n)

str = input('Input string for check: ')

print(check_string_in_list(new_list, str))
.................................

2.вариант
def create_string_list(number):
list = []
for i in range(number):
list.append(input('Введите что-нибудь: '))
return list

def check_double_first_value(list, find):
check = 0
find_index = -1
for i in range(len(list)):
if list[i] == find:
check += 1
if check == 2:
find_index = i
break

return find_index

size = int(input('Введите размер списка: '))
list = create_string_list(size)
find = input('Ищем: ')
if check_double_first_value(list, find) == (-1):
print('Нет повторов')
else:
print(f'Искомый элемент стоит на {check_double_first_value(list,find)} позиции.')

Домашняя работа

Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.

*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10

