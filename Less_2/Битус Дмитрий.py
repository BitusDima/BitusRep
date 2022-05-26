from sys import builtin_module_names
from termios import NOFLSH


homework1 = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'

fat = '\033[1m'
nofat= '\033[0;0m'
print('Шаг 1 - ' + fat + 'Количество символов -' + nofat, len(homework1))      
print()

homework11 = homework1[::-1]
print('Шаг 2 - ' + fat + 'Развернутая строка - ' + nofat, homework11)
print()

print('Шаг 3 - ' + fat + 'Каждое слово с большой буквы - ' + nofat, homework1.title(), end='\n\n')

print('Шаг 4 - ' + fat + 'Весь текст прописными буквами - ' + nofat, homework1.upper(), end='\n\n')

print('Шаг 5 - ' + fat + 'Число вхождений "нд" - ' + nofat, homework1.count('нд'))
print(fat + 'Число вхождений "ам" - ' + nofat, homework1.count('ам'))
print(fat + 'Число вхождений "о" - ' + nofat, homework1.count('о'), end='\n\n')

print(fat + 'Текст строчными буквами - '+ nofat, homework1.lower(), end='\n\n')

print(fat + 'Замена всех "о" на  "АА" - ' + nofat, homework1.replace('о','АА'), end='\n\n')

print(fat + 'Вывод каждого третьего символа - ' + nofat, homework1[0::3], end='\n\n')

name = input('Введите имя: ')
year = input('Введите год рождения: ')
print(fat + 'Вывод имени и года рождения - {}\t{}'.format(name, year) + nofat, end='\n\n')

print('Шаг 7 - ' + fat + 'Исходная строка" - ' + nofat, homework1)
