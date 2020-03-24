from Ingénieur import Ingenieur


class Junior(Ingenieur):
    def __init__(self, n2, p2, sa, i, ye, hor, nbp, nbg, exp):
        Ingenieur.__init__(self, n2, p2, sa, i, ye, hor, nbp, nbg)
        self.__exp = exp

    def afficher(self):
        return "* [id=" + str(self._identifiant) + "] Nom et prénom: " + self._nomsalarie + " " + self._prenom + ", Salaire: " + str(self._salaire) + ", Statut: Ingénieur-junior, Année d'embauche: " + str(self._embauche) + ", nombre de jours de travail: " + str(self._heures) + ", nombre d'heures de projet: " + str(self._projet) + ", nombre d'heures de gestion: " + str(self._gestion) + ", nombre d'années d'expérience: " + str(self.__exp) + " ans,"