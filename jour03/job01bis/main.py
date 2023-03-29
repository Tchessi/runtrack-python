#Créer un programme qui parcourt le contenu du fichier “data.txt” et qui compte le
#nombre de mots (sans caractère spéciaux) qui s’y trouvent.

import re

file = open('data.txt', 'r')

x = re.findall("\S+[a-zA-Z]",  file.read())
# print(x)
print('number of words is : ', len(x))


file.close()