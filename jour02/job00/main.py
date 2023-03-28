# Créez une classe “Personne” avec les attributs “nom”, “prenom”. Ajoutez une méthode
# “SePresenter()” qui affichera dans le terminal le nom et le prénom de la personne.
# Ajoutez aussi un constructeur prenant en paramètres de quoi donner des valeurs
# initiales aux attributs “nom” et “prenom”. Instanciez plusieurs personnes avec les
# valeurs de construction de votre choix et faites appel à la méthode “SePresenter()” afin
# de vérifier que tout fonctionne correctement. Ajouter un “accesseur” et un “mutateur”
# pour chacun des attributs.

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je m'appelle", self.nom, self.prenom)

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getPrenom(self):
        return self.prenom

    def setPrenom(self, prenom):
        self.prenom = prenom

# Création de deux instances de la classe Personne
p1 = Personne("De-Maison", "Jean-Francois")
p2 = Personne('Tchess', 'Pre')
p3 = Personne('Dorian', 'Sophie')

# Création de deux instances de la classe Personne
p1.SePresenter() 
p2.SePresenter()  # affiche "Je m'appelle Tchess Pre"

# Utilisation de l'accesseur getNom() pour récupérer le nom de la première personne
nom_personne1 = p1.getNom()
print(nom_personne1)  # affiche "De-Maison"

# Utilisation du mutateur setPrenom() pour changer le prénom de la deuxième personne
p2.setPrenom("Preza")
p2.SePresenter()  # affiche "Je m'appelle Tchess Preza"
