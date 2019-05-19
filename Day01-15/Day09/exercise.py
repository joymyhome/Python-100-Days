#%%
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def play(self):
        if self._age <= 16:
            print('do first kids')
        else:
            print('do second')


def main():
    person = Person('AA', 25)
    person.play()
    person.age = 15
    person.play()


if __name__ == '__main__':
    main()


#%%
class Person:

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('A')
        else:
            print('B')


def main():
    person = Person('A', 22)
    person.play()
    person._gender = 'man'


if __name__ == '__main__':
    main()

#%%
from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):  # * no need to pass self
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) *
                    (half - self._c))


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print('Not a valid triangle')


if __name__ == '__main__':
    main()

#%%
