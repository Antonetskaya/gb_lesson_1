#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds_polzovatel = int(input("Время в секундах: "))

hours = seconds_polzovatel // 3600
minutes = (seconds_polzovatel % 3600) // 60
seconds = (seconds_polzovatel % 3600) % 60

print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
