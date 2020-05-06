""" Модуль для операций """
from DataStructures.Carrier import Carrier

class Oper:
    def __init__(self, rule=lambda x, y: x + y):
        self.operation = rule

    def operation_properties(self):
        """ ХЗ если честно"""
        pass

    def partial_evaluation(self, **kwards):
        """ Тут тоже хз, в помощь functools.partial(почитайте доки) и в гугле 'partial evaluation'"""

    def Union(self, A: Carrier, B: Carrier):
        """ Эта функция возвращает объеденение двух множеств """
        temp = Carrier([])
        for i in A:
            temp.add(i)
        for i in B:
            temp.add(i)
        return temp

    def Intersection(self, A: Carrier, B: Carrier):
        """ Эта функция возвращает пересечение двух множеств """
        if A.__len__() >= B.__len__():
            temp_s = A
            temp_b = B
        else:
            temp_s = B
            temp_b = A
        temp = Carrier([])
        for i in temp_s:
            if i in temp_b:
                temp.add(i)
        return temp

    def Difference(self, A: Carrier, B: Carrier):
        """ Эта функция возвращает разницу двух множеств """
        temp = Carrier([])
        for i in A:
            if i not in B:
                temp.add(i)
        return temp

    def SymmetricDifference(self, A: Carrier, B: Carrier):
        """ Эта функция возвращает симметрическую разницу двух множеств """
        U = self.Union(A, B)
        temp = Carrier([])
        for i in U:
            if (i in A) and (i in B):
                continue
            else:
                temp.add(i)
        return temp

    def Union_2(self, *args):
        """
        TODO:
        Надо будет подумать как реализовать операции с семействами...
        """
        pass


if __name__ == "__main__":
    o = Oper()
    car_1 = Carrier([1, 2, 3])
    car_2 = Carrier([3, 5, 6])
    print(car_1, car_2)
    print('Union: ', o.Union(car_1, car_2))
    print(car_1, car_2)
    print('Intersection: ', o.Intersection(car_1, car_2))
    print(car_1, car_2)
    print('Difference: ', o.Difference(car_1, car_2))
    print(car_1, car_2)
    print('Symmetric Difference: ', o.SymmetricDifference(car_1, car_2))
    #print(car_1, car_2)
    #print(o.Union2(car_1, car_2))
