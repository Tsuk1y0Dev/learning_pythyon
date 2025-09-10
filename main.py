## Инициализация переменной
# a = int(input())

# if a != 0: #Проверка на ноль
#     if a % 2 == 0: #Проверка на чётность
#         print('Чётное')
#     else: 
#         print('Нечётное')
# else:
#     print("Нейтральное")

# Второе
## Инициализация переменной
# a = input()
##Вывод последней буквы
# print(a[-1])

#Третье TODO: нечувствительно к регистру 
# # Инициализация переменных
# first_word = input()
# second_word = input()
# Проверка на совпадение первых букв
# if first_word[0].lower() == second_word[0].lower():
#     print('Первые буквы совпадают')
# else:
#     print("Первые буквы разные")

# Четвёртое
# Инициализация переменной
# word = input()
## Проверка на "ь" в конце и вывод последней/предпоследней буквы
# if word[-1] == "ь":
#     print(word[-2])
# else:
#     print(word[-1])

#Пятое
# Инициализация переменной
# integer = input()
##Сложение первой и второй цифры двузначного числа
# print(int(integer[0]) + int(integer[-1]))

#Шестое
## Инициализация переменных
# first_integer = input()
# second_integer = input()
##Проверка на совпадение первых цифр чисел
# print(first_integer[0] == second_integer[0])

#Седьмое
# # Инициализация переменных
# first_integer = int(input())
# second_integer = int(input())
# # Проверка на кратность первого второму
# print(first_integer % second_integer == 0)

#Восьмое
# Инициализация переменной
# a = int(input())
# if a % 2 == 0: #Проверка на кратность двум
#     print('Кратное')
# else: 
#     print('Некратное')

#Девятое TODO: поддержка float
## Инициализация переменных
# first_integer = float(input())
# second_integer = float(input())
# third_integer = float(input())
## Проверка на возможность составления арифметической прогрессии из чисел
# if (third_integer - second_integer) == (second_integer - first_integer):
#     print('Из данных чисел можно составить арифметическую прогрессию')
# else:
#     print("нельзя")

#Десятое
# Инициализация переменной
# a = input()
# if len(a) == 3: #Проверка на количество цифр
#     print(int(a[0])*int(a[1])*int(a[2])) #Произведение цифр числа

#одинадцатое TODO: Добавлено количество одинаковых значений
# Инициализация переменных
# a = input()
# b = input()
# c = input()
# count:int = 0
## Проверка на равенство элементов с пополнением пар
# if a == b:
#     count += 1
# if b == c:
#     count += 1
# if a == c:
#     count += 1
# if count > 0: # Подсчёт количества совпадающих чисел
#     count += 1
# print(count)

#Двенадцатое
# Инициализация переменной
# integer = input()
# print(integer[0] == integer[1]) #Проверка на равенство цифр в числе