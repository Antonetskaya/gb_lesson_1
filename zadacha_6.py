#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Введите количество километров в первый день: "))
b = int(input("Введите количество километров желаемое: "))
nomer_dnya = 1
        
while a < b:
    a = a * 1.1
    nomer_dnya = nomer_dnya + 1
else:
    print("Номер дня: ", nomer_dnya)


