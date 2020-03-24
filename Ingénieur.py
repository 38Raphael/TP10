from Employé import Employee
from abc import ABC, abstractmethod


class Ingenieur(Employee, ABC):
    def __init__(self, n2, p2, sa, i, ye, hor, nbp, nbg):
        Employee.__init__(self, n2, p2, sa, i, ye, hor)
        self._projet = nbp
        self._gestion = nbg

    @abstractmethod
    def afficher(self):
        pass
