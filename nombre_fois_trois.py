# Douze suite de nombre multiplier par trois.
tour = 0                             # La variable pour les tours.
nombre = 1                           # La variable pour les nombres.

while tour < 12:                     # Le nombre de tour.
    nombre *= 3                      # A chaque tour fait x3 de la valeur précédente.
    print(nombre, end =" ")          # Affiche les nombre multipler par 3 suivis d'un espace.
    tour += 1                        # A chaque tour rajoute +1.