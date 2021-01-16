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
