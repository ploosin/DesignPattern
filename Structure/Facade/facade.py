# -*- encoding:utf-8 -*-

class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to the folks")
        self.hotelier = None
        self.florist = None
        self.caterer = None
        self.musician = None

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()
        self.florist = Florist()
        self.florist.set_flower_requirements()
        self.caterer = Caterer()
        self.caterer.set_cuisine()
        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def __is_available(self):
        print('Is the Hotel free for event on given day?')
        return True

    def book_hotel(self):
        if self.__is_available():
            print('Registered the booking')


class Florist(object):
    def __init__(self):
        print('Flower Decorations for the Event?')

    def set_flower_requirements(self):
        print("Carnations, Roses and Lilies would be used for Decorations")


class Caterer(object):
    def __init__(self):
        print('Food Arrangements for the Event')

    def set_cuisine(self):
        print('Chineses & Continental Cuisine to be served')


class Musician(object):
    def __init__(self):
        print('Musical Arrangements for the maariage')

    def set_music_type(self):
        print('Jazz and Classical will be played')


class You(object):
    def __init__(self):
        print('You:: Whoa! Marriage Arrangements?')

    def ask_event_manager(self):
        print('You:: Lets Contact the Event Manager')
        em = EventManager()
        em.arrange()

    def __del__(self):
        print('You:: Thanks to Event Manager, all preparations done! Phew')


if __name__ == '__main__':
    you = You()
    you.ask_event_manager()