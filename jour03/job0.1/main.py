#Créer un programme qui demande à l'utilisateur de renseigner une chaîne de caractères
#et qui écrit cette chaine de caractère dans un fichier “output.txt”.

def readString():
    file = open('output.txt', 'r') 
    print(file.read())
    file.close()

readString()