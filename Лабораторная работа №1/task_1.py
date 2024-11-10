# numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
#
# # TODO заменить значение пропущенного элемента средним арифметическим
#
# print("Измененный список:", ...)
#
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Шаг 1: Создаем список без None
valid_numbers = [num for num in numbers if num is not None]

# Шаг 2: Вычисляем среднее арифметическое и округляем до двух знаков после запятой
average = round(sum(valid_numbers) / len(valid_numbers), 2)

# Шаг 3: Создаем новый список с заменой None на среднее
result = [average if num is None else num for num in numbers]

print("Среднее арифметическое:", average)
print("Результат:", result)