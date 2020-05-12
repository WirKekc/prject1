class Test(object):
    def __add__(self, other):
        return '0_0'


t = Test()
print(t + 2)


class BadStr(str):
    def __add__(self, other):
        return str(self) + str(other)


t = BadStr('some')
print(t + 2)

class MathObject(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other

    def __ge__(self, other):
        return self.value >= other

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    # Operations:

    def __neg__(self):
        return -self.value

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        return self.value * other


class DictFunctionality(object):
    def __init__(self, values=None):
        if values is None:
            self.values = {}
        elif isinstance(values,dict):
            self.values = values
        else:
            raise ValueError()

    def __str__(self):
        return str(self.value) if self.value else ''

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    # Iteration:
    def __iter__(self):
        return iter(self.values)

    # 'in' operation:
    def __contains__(self, item):
        return item in self.values

    def __len__(self):
        return len(self.values)

