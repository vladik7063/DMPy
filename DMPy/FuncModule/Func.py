""" Модуль для работы со всюду определенными (тотальными) целочисленными функциями"""
from DataStructures.Carrier import Carrier


class Func:
    """ Класс обертки для взаимодействия с объектами модуля DMPy"""

    def __init__(self, func=lambda x: x):
        """
        :param func: принимаемая функция. По умолчанию стоит тождественное отображение
        """
        self.func = func
        self.domain = None

    """TODO: Переделать перегрузить метод __call__ (т.е. создать 2 метода __call__, один для типа 
    Carrier и другой для всего остального) с помощью декораторов

    Туториал: https://www.codementor.io/@arpitbhayani/overload-functions-in-python-13e32ahzqt """

    def __call__(self, arg):
        """ __call__ позволяет такой синтаксис:

        new_fun = Func(func=x**2)  # Инициализируем объект класса Func
        result = new_fun(3) # result = 9

    """
        if type(arg) == Carrier:
            return Carrier([self.func(x) for x in arg])
        return self.func(arg)


    def generate_image(self, domain: Carrier):
        """ Генератор образа отображения """
        for i in domain:
            yield self.func(i)

    """TODO:
    Перегрузить метод (т.е. создать с таким же названием, но другой) (опять же с помощью декоратора) так, чтобы его можно было применять не только к типу Carrier,
    но и к одному элементу"""

    def generate_orbit(self, domain: Carrier, depth=3, shape='matrix') -> Carrier:
        """
    Метод для составления орбит элементов относительно данной функции (т.е. f(f(f..(f(x))..)) )

    Если shape='matrix', возвращает Carrier, элементами которого являются другие Carrier'ы (матрица короче), где return_value[0] - это domain,
    return_value[1] - f(domain), return_value[2] - f(f(domain)) и т.д.

    Если shape='flat', то возвращает одномерный Carrier, где return_value[i] = f(f..(f(domain[i]))
    @:param domain: множество действия функции
    @:param depth: сколько раз мы применяем функцию к предыдущему результату
    @:param shape: 'matrix', 'flat'
    """
        orbits = {} #{j: Carrier([]) for j in domain}
        for i in range(depth):
            for j in domain:
                orbits[j].add(self.func(j))
        """ допишется... """


    def function_properties(self):
        """ Хз че тут делать, но для начала можно проверить сюръективонсть-инъективность-биективность,
        ну и другие свойства, которые у нас есть"""
        pass


if __name__ == "__main__":
    f = Func() #func=lambda x: x ** 2
    #print(f(Carrier(n=5)))

    print(f.generate_orbit(Carrier([1, 2, 3])))
