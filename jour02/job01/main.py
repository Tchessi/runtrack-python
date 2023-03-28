# Créer une classe “Livre” avec comme attribut un “titre” qu’elle reçoit en paramètre à la
# construction et une référence vers une classe “Auteur”. Ajouter une méthode “print”
# permettant d’afficher dans le terminal le titre du livre. Créer une classe “Auteur” héritant
# de la classe “Personne” recevant un nom et un prénom en paramètre de construction.
# La classe auteur devra posséder une collection de livres nommée "œuvre" en attribut
# ainsi qu’une méthode “listerOeuvre” affichant dans le terminal la liste des livres écrits
# par l’auteur. Ajouter à la classe Auteur une méthode “ecrireUnLivre” prenant en
# paramètre un titre de livre à écrire et générer une instance de la classe livre avec ce
# titre. Ajouter ce nouveau livre à l’oeuvre de l’auteur

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        if len(self.oeuvre) == 0:
            print(f"{self.nom} {self.prenom} n'a encore rien écrit.")
        else:
            print(f"{self.nom} {self.prenom} a écrit :")
            for livre in self.oeuvre:
                print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)


auteur1 = Auteur("Napoleon", "Hill")

auteur2 = Auteur('Tchessi', 'Pre')
auteur2.listerOeuvre()

auteur1.ecrireUnLivre("Réfléchissez et devenez riche")
auteur1.ecrireUnLivre("La maîtrise de la persuasion")
auteur1.listerOeuvre()  # Napoléon Hill a écrit :
                        # Réfléchissez et devenez riche
                        # La maîtrise de la persuasion

livre1 = auteur1.oeuvre[0]
livre1.print()  #Réfléchissez et devenez riche



