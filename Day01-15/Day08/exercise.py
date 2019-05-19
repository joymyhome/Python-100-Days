#%%
import time
#* 练习1：定义一个类描述数字时钟


class Clock:
    """A digital clock
    """

    def __init__(self, hour=0, minute=0, second=0):
        """Initialization
        
        Keyword Arguments:
            hour {int} -- [hour] (default: {0})
            minute {int} -- [minute] (default: {0})
            second {int} -- [second] (default: {0})
        """
        self._hour = hour  #* 可以访问 __就报错
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minCute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return f'{self._hour:02d}:{self._minute:02d}:{self._second:02d}'


def main():
    clock = Clock(23, 59, 58)
    while (True):
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()

#%%
from math import sqrt


class Point:
    """Point class
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        """
        move to (x, y)
        
        Arguments:
            x {num} -- new x position
            y {num} -- new y position
        """
        self.x = x
        self.y = y

    def distance_to(self, p):
        """
        calculate distance between self to Point p
        
        Arguments:
            p {Point} -- Another point
        
        Returns:
            num -- distance between self to other point
        """
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __str__(self):
        return f'({self.x}, {self.y})'


def main():
    point1 = Point(3, 5)
    point2 = Point(1, 6)
    print(point1.distance_to(point2))


if __name__ == '__main__':
    main()
#%%


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)


def main():
    test = Test('hello')
    test._Test__bar() #*虽然被mangled,但是也可以有方法访问
    print(test._Test__foo)


if __name__ == '__main__':
    main()

#%%


#%%
