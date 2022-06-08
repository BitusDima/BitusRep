a = int(input("Введите первое число: "))    # вводим данные
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print()

z = a and b and c and "Нет нулевых значений!!!"
print(z)

x = a or b or c or "Введены все нули!"
print(x)

if a > (b + c):
    print( a - b - c)

if a < (b +c):
    print(b + c - a)

if a > 50 and (b > a or c > a):
    print("Вася")

if a > 5 and b == 7 and c == 7:
    print("Петя")
    