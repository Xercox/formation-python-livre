#4.9 Écrivez un programme qui affiche la suite de symboles suivante :
#*
#**
#***
#****
#*****
#******
#*******
tour = 0                 # je crée mes tours qui commence a 0
etoile = ""             # Je crée mon étoile vide
while tour <7:           # je choisis le nombre de tour
    tour += 1            # je rajoute + 1 au compteur de tour
    etoile += '*'        # je rajoute une étoile par ligne
    print(etoile)        # résultat