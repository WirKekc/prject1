# Реализовать декоратор, который будет считать, сколько раз выполнялась функция
class Counter(object):
    instance = {}

    # @staticmethod
    def dec3(func):

        def how_match():

            if func.__name__ in Counter.instance.keys():
                Counter.instance[func.__name__] += 1
            else:
                Counter.instance[func.__name__] = 1
            print('{} is called {} times'.format(func.__name__, Counter.instance[func.__name__]))

            return func()

        return how_match


@Counter.dec3
def func123():
    a = 0
    for i in range(0, 150):
        a += i
    return a


func123()
func123()
func123()
func123()
