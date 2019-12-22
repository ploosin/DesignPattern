from abc import ABCMeta, abstractmethod


# AbstractClass
class Trip(metaclass=ABCMeta):
    @abstractmethod
    def set_transport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def return_home(self):
        pass

    def itinerary(self):
        self.set_transport()
        self.day1()
        self.day2()
        self.day3()
        self.return_home()


# Concrete Class
class VeniceTrip(Trip):
    def set_transport(self):
        print('Take a boat and find your way in the Grand Canal')

    def day1(self):
        print('Visit St Marks Basilica in ST Marks Square')

    def day2(self):
        print('Appreciate Doges Palace')

    def day3(self):
        print('Enjoy the food near the Rialto Bridge')

    def return_home(self):
        print('Get souvenirs for friends and get back')


class MaldivesTrip(Trip):
    def set_transport(self):
        print('On foot, on any island, Wow!')

    def day1(self):
        print('Enjoy the marine life on Banana Reef')

    def day2(self):
        print('Go for the water sports and snorkelling')

    def day3(self):
        print('Relax on the beach and enjoy the sun')

    def return_home(self):
        print('Dont feel like leaving the beach..')


# Client
class TravelAgency:
    def arrange_trip(self):
        choice = input('What kind of place youd like to go historical or to a beach?')
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()


TravelAgency().arrange_trip()
