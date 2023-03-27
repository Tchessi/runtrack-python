# Créer un programme qui demandera à l’utilisateur de renseigner un mot et un seul, sans
# espace ni aucun autre caractère que les 26 lettres de l’alphabet (sans accent ni
# majuscule).
# Votre programme devra modifier ce mot, en y changeant de place certains caractères
# (ou tous) afin de donner un mot plus “loin” dans l’ordre alphabétique que le mot
# renseigné par l'utilisateur.
# Attention: Le nouveau mot doit être le mot le plus proche possible, dans l’ordre
# alphabétique, du mot original !
# Par exemple, “abcde” donnerait “abced”. “acedb” est aussi “valide” mais n’est PAS le
# plus proche du mot original dans l’ordre alphabétique.

def triDeMot():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    result = input('Ecrivez une suite de lettres: ')
    new = ""
    
    for letter in result:
        if letter not in alphabet:
            print("Le mot doit contenir seulement des lettres de l'alphabet sans accent ni majuscule.")
            return

    for letter in result:
        i = alphabet.index(letter)
        if i == 25:
            new += letter
        else:
            new += alphabet[i+1]
            
    print("Le nouveau mot est :", new)

triDeMot()
