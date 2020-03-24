class Multinationale:
    def __init__(self, name, country):
        self.__nom = name
        self.__pays = country
        self.__filiale = []
        self.__nbsalary = 0
        self.__dateref = 3000
        self.__old = ""
        self.__nbsalary2 = 0

    def ajouterfiliale(self, obj):
        self.__filiale.append(obj)

    def afficher(self):
        for elm in self.__filiale:
            self.__nbsalary += len(elm.getsalary())
            if elm.getdate() < self.__dateref:
                self.__dateref = elm.getdate()
                self.__old = elm.getnom()
        for elm in self.__filiale:
            if elm.getnom == self.__old:
                self.__nbsalary2 += len(elm.getsalary())
        print("- La multinationale", self.__nom, "est composée de", len(self.__filiale), "filiales. Son pays d'origine est", self.__pays, ".\n- La filiale la plus ancienne de cette multinationale est:", self.__old, ". Elle est composée de", self.__nbsalary2, "salariés.\n", self.__nom, "est composée de", self.__nbsalary, "salariés:")
#        print("- La multinationale " + self.__nom + " est composée de " + str(len(self.__filiale)) + "filiales. Son pays d'origine est " + self.__pays + ".\n- La filiale la plus ancienne de cette multinationale est: " + self.__old + ". Elle est composée de " + str(self.__nbsalary2) + "salarié" + "s." if self.__nbsalary > 1 else "." + "\n" + self.__nom + " est composée de " + str(self.__nbsalary) + " salarié" + "s:" if self.__nbsalary > 1 else ":")
        for elm in self.__filiale:
            for elm2 in elm.getsalary():
                print(elm2.afficher() + ", site: " + elm.getsite() + ".")
