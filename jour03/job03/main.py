#Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre
#d'occurrence de chaque lettre (Minuscules et Capitales comptent pour la même lettre).
#A l’aide du module MatPlotLib, générer un histogramme représentant le pourcentage
#d’apparition de chaque lettre.

import matplotlib.pyplot as plt

# Ouvrir le fichier et lire le contenu
with open('data.txt', 'r') as file:
    content = file.read()

# Convertir en minuscules
content = content.lower()

# Initialiser un dictionnaire pour compter les occurrences de chaque lettre
occurrences = {}

# Parcourir chaque lettre du contenu
for letter in content:
    # Ignorer les caractères qui ne sont pas des lettres
    if not letter.isalpha():
        continue
    # Incrémenter le compteur d'occurrences pour cette lettre
    if letter in occurrences:
        occurrences[letter] += 1
    else:
        occurrences[letter] = 1

# Calculer le total des occurrences
total_occurrences = sum(occurrences.values())

# Calculer le pourcentage d'apparition de chaque lettre
percentages = {}
for letter, count in occurrences.items():
    percentages[letter] = (count / total_occurrences) * 100

# Créer un histogramme à partir des pourcentages d'apparition
plt.bar(percentages.keys(), percentages.values())
plt.xlabel('Lettres')
plt.ylabel('% d\'apparition')
plt.show()
