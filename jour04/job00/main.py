# Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre
# programme devra calculer la factorielle de ce nombre, sans utiliser de fonction autre
# que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach ni ... boucle.
# Seulement de la récursivité.

def factorielle(n):
    if n == 0: # si on donne 0 y'a rien a calculer
        return 1
    else:
        F = 1
        print(str(n) + "n")
        for k in range(2,n+1): # +1 sinon il manquera une valeur , du style au < 6 // =< 5
            print(k)
            F = F * k
        return F # une fois que n a été multiplié par tous ses facteurs alors on return le le resultant 
                # on multiplie les facteurs dans l'ordre croissant et on s'arrete lorsque la portée de k atteint celle du foreach
                

print(factorielle(5)) 