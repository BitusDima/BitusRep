
#white = '\u2B1C'
#black = '\u2B1B'


# пишем словари со всеми нарисованными цифрами и типами разделителей

from mimetypes import init


zero = {
1: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
2: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
3: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
4: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
5: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
6: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
7: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B'
}
one = {
1: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B', 
2: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B', 
3: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B', 
4: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B', 
5: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B', 
6: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B', 
7: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B'
}
two = {
1: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
2: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
3: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
4: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B',
5: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B',
6: '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
7: '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B'
}
three = {
1: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
2: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
3: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
4: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
5: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
6: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
7: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B'
}
four = {
1: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
2: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B',
3: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B',
4: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B',
5: '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
6: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B',
7: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B'
}
five = {
1: '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B',
2: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
3: '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
4: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
5: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
6: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
7: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B'
}
six = {
1: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
2: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
3: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
4: '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
5: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
6: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
7: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B'
}
seven = {
1: '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B',
2: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
3: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B',
4: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B',
5: '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
6: '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
7: '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B'
}
eight = {
1: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
2: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
3: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
4: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
5: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
6: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
7: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B'
}
nine = {
1: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B',
2: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
3: '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
4: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B',
5: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
6: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B',
7: '\u2B1B' '\u2B1C' '\u2B1C' '\u2B1C' '\u2B1B' '\u2B1B'
}
separator_1  = { 
1: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B', 
2: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B', 
3: '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B', 
4: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',  
5: '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B' '\u2B1B', 
6: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
7: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' 
}
separator_2 = {
1: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B', 
2: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B', 
3: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B', 
4: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',  
5: '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B' '\u2B1B', 
6: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
7: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' 
}
separator_3 = {
1: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B', 
2: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B', 
3: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B', 
4: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',  
5: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1C' '\u2B1B', 
6: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B',
7: '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' '\u2B1B' 
}

# запускаем бесконечный цикл для вывода времени
while True:

    # получаем точное время и переводим его в строчный формат
    import datetime
    timenow = str(datetime.datetime.now().time())   

    # функция для присвоения каждой цифре времени соответствующего нарисованного словаря (i- индекс цифры в строке timenow)
    def seek_digit(i):
        if timenow[i] == '0':
            h = zero
        elif timenow[i] == '1':
            h = one
        elif timenow[i] == '2':
            h = two
        elif timenow[i] == '3':
            h = three
        elif timenow[i] == '4':
            h = four
        elif timenow[i] == '5':
            h = five
        elif timenow[i] == '6':
            h = six
        elif timenow[i] == '7':
            h = seven
        elif timenow[i] == '8':
            h = eight
        elif timenow[i] == '9':
            h = nine
        return h
   

    # построчный вывод времени из всех словарей 
    for numb_str in range(1, 8):
        if timenow[7] == '1' or timenow[7] == '4' or timenow[7] == '7' or timenow[7] == '0':    # первый тип разделителей
            print(seek_digit(0)[numb_str] + seek_digit(1)[numb_str] + separator_1[numb_str] +
            seek_digit(3)[numb_str] + seek_digit(4)[numb_str] + separator_1[numb_str] +
            seek_digit(6)[numb_str] + seek_digit(7)[numb_str])

        if timenow[7] == '2' or timenow[7] == '5' or timenow[7] == '8':                         # второй тип разделителей
            print(seek_digit(0)[numb_str] + seek_digit(1)[numb_str] + separator_2[numb_str] +
            seek_digit(3)[numb_str] + seek_digit(4)[numb_str] + separator_2[numb_str] +
            seek_digit(6)[numb_str] + seek_digit(7)[numb_str])

        if timenow[7] == '3' or timenow[7] == '6' or timenow[7] == '9':                         # третий тип разделителей
            print(seek_digit(0)[numb_str] + seek_digit(1)[numb_str] + separator_3[numb_str] +
            seek_digit(3)[numb_str] + seek_digit(4)[numb_str] + separator_3[numb_str] +
            seek_digit(6)[numb_str] + seek_digit(7)[numb_str])

    # замораживаем выполнение на 0,25 секунды
    import time
    time.sleep(0.25)

    # очищаем экран
    import os
    os.system('clear')
    







