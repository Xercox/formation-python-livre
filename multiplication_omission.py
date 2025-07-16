# Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13,
# mais n’affiche que ceux qui sont des multiples de 7.

tour = 0                                    # La variable pour les tours.     
multiple_treize = 0                         # La variable pour les multiples de 13.

while tour < 50 :                           # Demande à faire 50 tours.
    tour += 1                               # Rajout de tour par boucle.
    multiple_treize += 13                   # Rajoute +13 au multiple de 13.
    if (multiple_treize % 7 == 0):          # Si le multiple de 13 est aussi un multiple de 7. 
        print(multiple_treize, end = " ")   # Affichage du multiple suivis d'un espace
