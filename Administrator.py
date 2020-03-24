from Employé import Employee


class Admninistrator(Employee):
    def __init__(self, n2, p2, sa, i, ye, hor, se):
        Employee.__init__(self, n2, p2, sa, i, ye, hor)
        self.__service = se

    def afficher(self):
        return "* [id=" + str(self._identifiant) + "] Nom et prénom: " + self._nomsalarie + " " + self._prenom + ", Salaire: " + str(self._salaire) + ", Statut: Administratif, Année d'embauche: " + str(self._embauche) + ", nombre de jours de travail: " + str(self._heures) + ", service: " + self.__service