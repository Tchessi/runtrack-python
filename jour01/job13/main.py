# Créez un programme qui demande 5 fois à l’utilisateur de renseigner un nombre entier.
# Stockez ces nombres entiers dans une liste puis triez-les par ordre croissant avant de
# les afficher, dans l’ordre, dans le terminal.

# demander à l'utilisateur de renseigner 5 nombres entiers
numbers = []
for i in range(5):
    number = int(input("Entrez un nombre entier :"))
    numbers.append(number)

# trier les nombres par ordre croissant
numbers.sort()

# afficher les nombres triés dans le terminal
print("Les nombres triés par ordre croissant sont :")
for number in numbers:
    print(number)