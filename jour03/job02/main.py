#Créer un programme qui demande à l’utilisateur de renseigner un nombre entier. Le
#programme devra alors parcourir le contenu du fichier “data.txt” compter le nombre de
#mots de la taille renseignée qui s’y trouvent.

import re
val = int(input("Entrez un nombre entier: "))

folder = open("./data.txt", "r")
x = folder.read()

word = re.findall("[\w']+", x)

a = 0
i = 0

while i < len(word):
    if len(word[i]) == val:
        a += 1
    i += 1

print("Resultat", a)