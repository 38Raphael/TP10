from Salarié import Salarie
from abc import ABC, abstractmethod


class Employee(Salarie, ABC):
    def __init__(self, n2, p2, sa, i, ye, hor):
        Salarie.__init__(self, n2, p2, sa, i)
        self._embauche = ye
        self._heures = hor

    @abstractmethod
    def afficher(self):
        pass
