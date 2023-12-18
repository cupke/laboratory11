def multiply_until_zero():
    result = 1  # Инициализируем результат умножения единицей

    while True:
        try:
            number = float(input("Введите число (введите 0 для завершения): "))
            if number == 0:
                break  # Выход из цикла при вводе 0
            result *= number  # Умножаем текущее число на результат
        except ValueError:
            print("Ошибка! Введите корректное число.")

    return result

# Вызываем функцию и выводим результат на экран
result = multiply_until_zero()
print("Произведение введенных чисел:", result)
