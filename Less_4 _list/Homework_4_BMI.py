
print("Введите Ваш рост в метрах: ")
h = float(input())                           # вводим рост
print("Введите Ваш вес в килограммах: ")
m = float(input())                           # вводим вес    
print("Введите Ваш возраст: ")
age = float(input())                         # вводим возраст    
print("Введите Ваш пол (М/Ж): ")
gender = input()                             # вводим пол    

BMI = round(m / h ** 2)                        # высчитываем BMI
print('Ваш индекс массы тела:', BMI)
print()
before = BMI - 10                              # производим рассчеты для построения шкалы  
after = 60 - BMI
print("10", "=" * before +  "|" + "=" * after, "60")  # выводим шкалу 
print()

if gender == "М":                                       # даем рекомендации в зависимости от пола, возроста и                
    if age >= 15 and age <= 60:
        if BMI <= 18:
            print("Больше кушай, займись спортом!")
        elif BMI >= 30:
            print("Меньше кушай, займись спортом!")
        else:
            print("Всё норм, живи как жил!")
    if age < 15:
        print("Главное хорошо учиться в школе")
    if age > 60:
        print("Думайте лучше о рыбалке")
if gender == "Ж":
    if age >= 15 and age <= 60:
        if BMI <= 18:
            print("Может стоит набрать вес?")
        elif BMI >= 30:
            print("Может стоит похудеть?")
        else:
            print("Всё норм!")
    if age < 15:
        print("Главное хорошо учиться в школе")
    if age > 60:
        print("Думайте о внуках, BMI подождет")