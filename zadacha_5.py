#5.  Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с
# прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

vyruchka = float(input("Введите сумму выручки "))
izderzhki = float(input("Введите сумму издержек "))
pribyl = vyruchka - izderzhki

if vyruchka > izderzhki:
    rentabelnost = pribyl / vyruchka
    print("Фирма работает с прибылью: ", pribyl, "Рентабельность составляет: ", rentabelnost)
    sotrudniki = int(input("Введите количество сотрудников фирмы: "))
    pribyl_na_1_sotrudnika = pribyl / sotrudniki
    print("Прибыль на одного сотрудника составляет: ", pribyl_na_1_sotrudnika)

elif vyruchka < izderzhki:
    print("Фирма работает в убыток: ", pribyl)
    
else:
    print("Фирма работает в ноль") # выручка и издержки равны
