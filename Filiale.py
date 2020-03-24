class Filiale:
    def __init__(self, n, p, d):
        self.__name = n
        self.__country = p
        self.__creationdate = d
        self.__salaryman = []

    def ajoutersal(self, obj):
        self.__salaryman.append(obj)

    def supprsal(self, obj):
        self.__salaryman.remove(obj)

    def getsalary(self):
        return self.__salaryman

    def getdate(self):
        return self.__creationdate

    def getsite(self):
        return self.__country

    def getnom(self):
        return self.__name
