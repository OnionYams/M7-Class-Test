

class Animal:
    """Animal class"""
    def __init__(self, name):
        print('Initializing name')
        self.__name = name

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name

    def eat(self):
        print('Animal Eating')

    def move(self):
        print('Animal Moving around')

class Vehicle:
    """Vehicle class"""
    def __init__(self, name):
        print('Initializing name')
        self.__name = name

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name

    def fuel(self):
        print('Fueling Vehicle')
    
    def transport(self):
        print("Transporting something")

class Book:
    """Book class"""
    def __init__(self, name, author):
        print('Initializing name')
        self.__name = name
        self.__author = author

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name

    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name

    @property
    def author(self):
        print('Getting author')
        return self.__author

    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name

    def read(self):
        print('Reading Book')
    