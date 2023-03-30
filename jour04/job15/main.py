# Écrire un programme qui demande à l’utilisateur de fournir une première chaîne de
# caractères, puis une seconde. Le programme affiche 1 si les 2 chaines sont identiques
# ou 0 si les chaînes ne sont pas identiques. Les chaînes ne sont constituées que de
# lettres minuscules. La deuxième chaîne de caractères peut contenir un ou plusieurs ‘ * ‘.
# Chaque ‘ * ‘ peut remplacer 0 ou plusieurs caractères. Par exemple, si la chaîne 1 est
# “laplateforme” et la chaine 2 “lap*”, le programme affiche 1 car l’ ‘ * ‘ remplace ‘
# lateforme ‘. Si la chaîne 1 est “laplateforme” et la chaîne 2 “l*a*pla*te*form***e” le
# programme renvoie 1 car les ‘ * ‘ ne remplace rien.

def compare_chaines(chaine1, chaine2):
    if len(chaine1) != len(chaine2) and '*' not in chaine2:
        return 0

    i, j = 0, 0
    while i < len(chaine1) and j < len(chaine2):
        if chaine2[j] == '*':
            j += 1
            while j < len(chaine2) and chaine2[j] == '*':
                j += 1
            if j == len(chaine2):
                return 1
            while i < len(chaine1) and chaine1[i] != chaine2[j]:
                i += 1
            if i == len(chaine1):
                return 0
        elif chaine1[i] == chaine2[j]:
            i += 1
            j += 1
        else:
            return 0
    if i == len(chaine1) and j == len(chaine2):
        return 1
    else:
        return 0

chaine1 = input("Entrez la première chaîne : ")
chaine2 = input("Entrez la deuxième chaîne : ")
resultat = compare_chaines(chaine1, chaine2)
print(resultat)
