#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

chislo = int(input("Введите любое число больше 100: "))
a = 0

while (chislo):
    if chislo % 10 > a:
        a = chislo % 10
    chislo //= 10
print(a)