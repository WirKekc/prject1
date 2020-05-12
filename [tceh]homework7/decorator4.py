# Реализовать декоторатор, который будет логгировать процесс выполнения функции: создан декоратор, начато выполнение
# функции, закончено выполнение функции
def dec4(func):
    print('Создан декоратор')
    def log():
        print('Начато выполнение функции {}'.format(func.__name__))
        func_return = func()
        print('Закончено выполнение функции{}'.format(func.__name__))
        return func_return
    return log

@dec4
def func123():
    a = 0
    for i in range(0, 150):
        a += i
    return a


func123()
func123()