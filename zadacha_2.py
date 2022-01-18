#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds_polzovatel = int(input("Время в секундах: "))

hours = seconds_polzovatel // 3600
print(hours)  # для проверки

minutes = int(seconds_polzovatel % 3600 / 60)
print(minutes)  # для проверки

seconds = int(seconds_polzovatel % 60)
print(seconds) # для проверки

print(hours, ":", minutes, ":", seconds)
