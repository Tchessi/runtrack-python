# Luke Skywalker, un professeur de Math, fait passer un test et décide de noter ses élèves
# sur une échelle allant de 0 à 100 inclus.
# Si un étudiant obtient moins de 40 sur 100, il échoue au test.
# S'il a plus de 40, il réussit le test. Luke est un professeur fort sympathique et décide
# donc d’arrondir à la hausse les notes des étudiants ayant réussi le test. Mais Luke n’est
# quand même pas trop gentil. Cet arrondi à la hausse ne bénéficiera qu’aux étudiants
# remplissant certains critères car, tout de même, il ne faut pas exagérer, sans blague.
# Le critère est simple: Si un étudiant a eu une note de moins de strictement 3 points de
# son prochain multiple de 5, alors sa note est arrondie à ce multiple de 5. Par exemple,
# un 83 sera arrondi à 85 alors qu’un 82 restera un 82.
# Pour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre une liste
# de notes et qui renvoie une liste de notes, arrondies comme il se doit, quand cela est
# nécessaire.

tab = {'zor' : 40, 'blog' : 35, 'zorus' : 52, 'zozor' :66, 'orzo' : 82, 'zozr' : 83,'rozr' : 94, 'zorzo' : 92,'rozoz' : 99}
new_result = {}
for key, data in tab.items():
    if(data < 40):
        print(key + ' : ' + str(data) + ' Test echoué')
    else:
        #inf
        # if data % 5 == 1:
        #     data = data -1
        # if data % 5 == 2:
        #     data = data -2
        #sup
        if data % 5 == 3:
            data = data + 2
        if data % 5 == 4:
            data = data + 1
        
        print( key + ' : ' + str(data) + ' Test réussi')

print(81%5)
print(82%5)
print(83%5)
print(84%5)