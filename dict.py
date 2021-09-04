#Создайте словарь:
#{"city": "Москва", "temperature": "20"}
#Выведите на экран значение ключа city
#Уменьшите значение "temperature" на 5
#Выведите на экран весь словарь

#Создайте словарь
weather = {"city": "Москва", "temperature": "20"}

#Выведите на экран значение ключа city
print(weather.get("city"))

#Уменьшите значение "temperature" на 5
weather["temperature"] = int(weather["temperature"]) - 5
print(weather)

# Проверьте, есть ли в словаре ключ country

print(weather.get("country"))

# Выведите значение по-умолчанию "Россия" для ключа country

print(weather.get("country", "Россия"))

# Добавьте в словарь элемент date со значением "27.05.2019"

weather["date"] = "27.05.2019"

# Выведите на экран длину словаря

print(len(weather))
# print(type(weather))
