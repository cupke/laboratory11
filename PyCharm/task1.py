def positive():
    print("Положительное")
def negative():
    print("Отрицательное")
def test():
    pass
if __name__ == '__main__':
    try:
        num = int(input("Введите целое число: "))
        if num > 0:
            positive()
        elif num < 0:
            negative()
        else:
            print("Ноль")
        test()
    except ValueError:
        print("Ошибка! Введите целое число.")
