# Créer un programme qui parcourt le contenu du fichier “domains.xml” et qui compte le
# nombre d’extension de domaines qui s’y trouvent (.com, .net, etc ...).
import re

file = open('domains.xml', 'r')
file2 = open('domains.xml', 'r') 

net = '.net'
com = '.com'
dot_net_number = re.findall(".net",  file.read())
dot_com_number = re.findall(".com",  file2.read())
print('dot_net_number', ':')
print(len(dot_net_number))
print('dot_com_number', ':')
print(len(dot_com_number))
file.close()