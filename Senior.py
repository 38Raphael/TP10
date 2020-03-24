from Ingénieur import Ingenieur


class Senior(Ingenieur):
    def __init__(self, n2, p2, sa, i, ye, hor, nbp, nbg, resp):
        Ingenieur.__init__(self, n2, p2, sa, i, ye, hor, nbp, nbg)
        self.__responsability = resp

    def afficher(self):
        return "* [id=" + str(self._identifiant) + "] Nom et prénom: " + self._nomsalarie + " " + self._prenom + ", Salaire: " + str(self._salaire) + ", Statut: Ingénieur-senior, Année d'embauche: " + str(self._embauche) + ", nombre de jours de travail: " + str(self._heures) + ", nombre d'heures de projet: " + str(self._projet) + ", nombre d'heures de gestion: " + str(self._gestion) + ", responsabilité: " + self.__responsability + ","