#Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre
#d'occurrence de chaque lettre (Minuscules et Capitales comptent pour la même lettre)
#en début de mot. A l’aide du module MatPlotLib, générer un histogramme représentant
#le pourcentage de présence de chaque lettre en début de mot.

import string
import matplotlib.pyplot as plt

# Initialisation du compteur
occurrences = {c: 0 for c in string.ascii_lowercase}

# Ouverture du fichier en lecture
with open("data.txt", "r") as f:
    # Parcours de chaque ligne du fichier
    for line in f:
        # Suppression des caractères de ponctuation et des espaces
        line = line.translate(str.maketrans("", "", string.punctuation))
        line = line.lower().split()
        # Comptage des occurrences de chaque lettre en début de mot
        for word in line:
            if word[0] in occurrences:
                occurrences[word[0]] += 1

# Calcul du pourcentage de présence de chaque lettre
total = sum(occurrences.values())
percentages = {c: occurrences[c]/total*100 for c in occurrences}

# Création du graphique
plt.bar(percentages.keys(), percentages.values())
plt.xlabel("Lettres en début de mot")
plt.ylabel("Pourcentage de présence")
plt.title("Histogramme de la présence des lettres en début de mot")
plt.show()
