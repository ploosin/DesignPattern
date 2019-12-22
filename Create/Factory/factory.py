# -*-encoding:utf-8-*-
from abc import ABCMeta, abstractmethod


# Product
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


# ConcreteProduct
class PersonalSection(Section):
    def describe(self):
        print('Personal Section')


class AlbumSection(Section):
    def describe(self):
        print('Album Section')


class PatentSection(Section):
    def describe(self):
        print('Patent Section')


class PublicationSection(Section):
    def describe(self):
        print('Publication Section')


# Creator
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_section(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)


# ConcreteCreator
class LinkedIn(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())


class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create? [LinkedIn or FaceBook]")

    profile = eval(profile_type)()
    print('Creating Profile...', type(profile).__name__)
    print('Profile has section --', profile.get_section())
