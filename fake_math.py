def divide(first, second):
    if second != 0:
        return first / second
    else:
        return 'Ошибка'

if __name__ == '__main__':
    print(divide(1,0))
