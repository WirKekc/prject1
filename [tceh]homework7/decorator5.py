# Реализовать декоратор, который будет перехватывать все исключения в функции. Если они случились, нужно просто писать
# в консоль сообщение об ошибке
def dec5(func):
    def catch_errors(*args, **kwargs):
        try:
            func_return = func(*args, **kwargs)
        except Exception as e:
            print('Function {} droped: {}'.format(func.__name__, e))


    return catch_errors

@dec5
def err_func(num):
    return num%2


err_func(1)
