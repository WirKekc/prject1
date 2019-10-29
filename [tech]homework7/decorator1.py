# Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
def canceled_decorator(cenc_dec):
    def external_func():
        print('{} is canceled!'.format(cenc_dec.__name__))
    return external_func



@canceled_decorator
def smth():
    print('lol')

smth()