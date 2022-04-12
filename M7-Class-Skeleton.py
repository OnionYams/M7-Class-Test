

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
        print('Animal moving around')

class Fish(Animal):
    def swim(self):
        print("Swimming about")
class Snake(Animal):
    def slither(self):
        print("Slithering about")
class Person(Animal):
    def talk(self):
        print("Talking about something")

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

    @property
    def manufacturer(self):
        print('Getting manufacturer')
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, new_manufacturer):
        print('Setting manufacturer')
        self.__manufacturer = new_manufacturer

    @manufacturer.deleter
    def manufacturer(self):
        print('Deleting manufacturer')
        del self.__manufacturer

    def fuel(self):
        print('Fueling Vehicle')
    
    def transport(self):
        print("Transporting something")
    
class Car(Vehicle):
    def drive(self):
        print("Driving car")
class Bicycle(Vehicle):
    def ride(self):
        print("Riding bike")
class Boat(Vehicle):
    def drive(self):
        print("Driving boat")
class big_balloon(Vehicle):
    def inflate(self):
        print("Inflating hot air balloon")


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

    @property
    def publishYear(self):
        print('Getting publication year')
        return self.__year

    @publishYear.setter
    def publishYear(self, new_year):
        print('Setting yeaer')
        self.__year = new_year

    @publishYear.deleter
    def publishYear(self):
        print('Deleting publication year')
        del self.__year


    def read(self):
        print('Reading Book')

class Textbook(Book):
    def study(self):
        print("Studying book")
class AddressBook(Book):
    def search(self):
        print("Searching for address")
    