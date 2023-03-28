# Créer une classe “Client” héritant de “Personne”, prenant en paramètre un nom et un
# prenom.
# Créez une classe “Bibliotheque” avec comme attributs un nom et un catalogue: une
# collection de livres ou chaque livre est associé à une quantité (représenté par un
# nombre entier). Ajoutez les méthodes suivantes :
# - acheterLivre: Prenant en paramètre un objet auteur, le nom d’un livre ainsi qu’un
# nombre entier représentant une quantité. Si le livre existe bien dans l'œuvre de
# l’auteur, ajouter ce livre au catalogue de la bibliothèque avec la quantité
# correspondante.
# - inventaire: Une méthode qui affiche dans le terminal les titres des livres présents
# dans le catalogue ainsi que leur quantité.
# - louer: Cette méthode reçoit en paramètres une instance d’objet “Client” ainsi que
# le nom d’un livre. Si le livre existe et est en stock, ajoutez ce livre à la collection
# de livre du client et tenez à jour la quantité de ce livre dans la bibliothèque.
# - rendreLivres: Une méthode qui prend un “Client” en paramètre et qui récupère
# tous les livres de ce dernier et les ajoute au catalogue de la bibliothèque.
# Ajouter à la classe “Client” un attribut collection étant une collection de livres et ajouter
# la méthode inventaire qui affiche dans le terminal les titres des livres en possession du
# client.

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

class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        if len(self.collection) == 0:
            print(f"{self.nom} {self.prenom} ne possède aucun livre.")
        else:
            print(f"{self.nom} {self.prenom} possède :")
            for livre in self.collection:
                print(livre.titre)

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                print(f"La bibliothèque a acheté {quantite} exemplaire(s) du livre {titre}.")
                return
        print(f"Le livre {titre} n'est pas disponible chez l'auteur {auteur.nom} {auteur.prenom}.")

    def inventaire(self):
        if len(self.catalogue) == 0:
            print(f"Le catalogue de la bibliothèque {self.nom} est vide.")
        else:
            print(f"La bibliothèque {self.nom} possède :")
            for livre, quantite in self.catalogue.items():
                print(f"{quantite} exemplaire(s) de {livre}")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            for livre in client.collection:
                if livre.titre == titre:
                    print(f"{client.nom} {client.prenom} a déjà loué le livre {titre}.")
                    return
            livre = Livre(titre, None)
            client.collection.append(livre)
            self.catalogue[titre] -= 1
            print(f"{client.nom} {client.prenom} a loué le livre {titre}.")
        else:
            print(f"Le livre {titre} n'est pas disponible.")

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.catalogue:
                self.catalogue[livre.titre] += 1
            else:
                self.catalogue[livre.titre] = 1
        client.collection = []
        print(f"{client.nom} {client.prenom} a rendu tous ses livres.")

# Créations des auteurs
auteur1 = Auteur("Hugo", "Victor")
auteur2 = Auteur("Flaubert", "Gustave")

# Affichage de l'inventaire de la bibliothèque avant l'achat de livre
auteur1.ecrireUnLivre("Titre 1")
auteur1.ecrireUnLivre("Titre 2")
auteur2.ecrireUnLivre("Titre 3")
print("----------------")

#Création de la bibliothèque
bibliotheque = Bibliotheque("Bibliotheque Alcazar")
print("----------------")

#Achat de livres par la bibliothèque
bibliotheque.acheterLivre(auteur1, "Les Misérables", 5)
bibliotheque.acheterLivre(auteur2, "Le Rouge et le Noir", 3)
bibliotheque.acheterLivre(auteur2, "Madame Bovary", 2)
print("----------------")

client1 = Client("Smith", "John")
client2 = Client("Will", "Jane")
print("----------------")

#Louer des livres par les clients
bibliotheque.louer(client1, "Les Misérables")
bibliotheque.louer(client1, "Le Rouge et le Noir")
bibliotheque.louer(client2, "Les Misérables")
bibliotheque.louer(client2, "Madame Bovary")
print("----------------")

#Affichage des livres en possession des clients
client1.inventaire()
client2.inventaire()
print("----------------")

#Affichage de l'inventaire de la bibliothèque après la location de livres
bibliotheque.inventaire()

print("----------------")
#Retour des livres des clients à la bibliothèque
bibliotheque.rendreLivres(client1)
bibliotheque.rendreLivres(client2)

print("----------------")
#Affichage de l'inventaire de la bibliothèque 
#après le retour des livres

bibliotheque.inventaire()
print("----------------")
#Affichage des livres en possession des clients après le retour des livres
client1.inventaire()
client2.inventaire()