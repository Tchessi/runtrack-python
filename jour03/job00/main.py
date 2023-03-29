# Créer un programme qui demande à l'utilisateur de renseigner une chaîne de caractères
# et qui écrit cette chaine de caractère dans un fichier “output.txt”.

def writeString():
    result = input("Veuillez saisir une chaine de caractères : ")
    file = open('output.txt', 'w') 
    file.write(result)
    file.close()

writeString()