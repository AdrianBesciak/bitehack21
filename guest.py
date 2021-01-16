class Guest:
    def __init__(self, name, surname, uuid, destination=None):
        self.__name = name
        self.__surname = surname
        self.__uuid = uuid
        self.__destination = destination

    def get_uuid(self):
        return self.__uuid

    def add_destination(self, destination):
        self.__destination = destination

    def get_destination(self):
        return self.__destination

    @staticmethod
    def get_guests():
        file = open('guests.txt', 'r')
        guests = []

        while file.readable():
            line = file.readline()
            if len(line) < 4:
                break
            words = line.split(';')
            guests.append(Guest(words[0], words[1], words[2], words[3][0:len(words[3])-1]))
        return guests

