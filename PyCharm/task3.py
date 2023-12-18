def get_input():
    #Запрашивает ввод с клавиатуры и возвращает полученную строку.
    user_input = input("Введите значение: ")
    return user_input

def test_input(value):
    #Проверяет, можно ли переданное значение преобразовать к целому числу.
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False

def str_to_int(value):
    #Преобразовывает переданное значение к целочисленному типу и возвращает полученное число.
    return int(value)

def print_int(value):
    #Выводит переданное значение на экран.
    print("Преобразованное значение:", value)

# Основная ветка программы
input_value = get_input()

if test_input(input_value):
    int_result = str_to_int(input_value)
    print_int(int_result)
else:
    print("Невозможно преобразовать введенное значение к целому числу.")
