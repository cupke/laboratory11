import math

def circle(radius):
    #Вычисляет площадь круга по формуле πr^2
    return math.pi * radius ** 2

def cylinder():
    #Вычисляет площадь боковой поверхности или полную площадь цилиндра
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    choice = input("Хотите получить только площадь боковой поверхности? (да/нет): ").lower()

    if choice == 'да':
        # Вычисляем и выводим площадь боковой поверхности
        lateral_area = 2 * math.pi * radius * height
        print("Площадь боковой поверхности цилиндра:", lateral_area)
    elif choice == 'нет':
        # Вычисляем и выводим полную площадь цилиндра
        lateral_area = 2 * math.pi * radius * height
        total_area = lateral_area + 2 * circle(radius)
        print("Полная площадь цилиндра:", total_area)
    else:
        print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")

# Вызываем функцию cylinder() из основной ветки программы
cylinder()
