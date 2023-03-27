# Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en
# fonction des paramètres d’entrées, (width, height), par exemple:
# draw_rectangle(10, 3)

# | --------|
# |        |
# | --------|

def rectangle(width, height):

    print('|'+ '-' * width + '|')
    for i in range(1,height):
        print('|' + ' ' *width + '|')
        # for x in range(1,width):
    print('|'+ '-' * width + '|')
    
width = input('Quelle largeur?')
height = input('Quelle hauteur?')
rectangle(int(width), int(height))