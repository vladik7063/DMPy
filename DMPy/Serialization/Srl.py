import pickle
from DataStructures.Carrier import Carrier


def dump(something, filename):
    """
    Функция сериализации объектов в памяти,
    принимаемые аргументы - сам объект и Ваше название для файла.
    """
    with open(rf'{filename}.pickle', 'wb') as file:
        pickle.dump(something, file)


def load(filename):
    """ Загрузка объекта из памяти, принимаемый аргумент - название файла."""
    with open(rf'{filename}.pickle', 'rb') as file:
        return pickle.load(file)
