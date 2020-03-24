from abc import ABC, abstractmethod


class Salarie (ABC):
    def __init__(self, n2, p2, sa, i):
        self._nomsalarie = n2
        self._prenom = p2
        self._salaire = sa
        self._identifiant = i

    @abstractmethod
    def afficher(self):
        pass
