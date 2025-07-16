# La solution du vieux sage sur échiquier qui demande 1 grain de riz sur la premiere case qui double de case en case.


case = 1                                                                                    # La base da ma boucle.
grains_de_riz = 1                                                                           # Ma variable pour le riz.

while case <= 64 :                                                                          # Ma boucle avec sa base et le nombre de tour.
    grains_scientifique = format(grains_de_riz, ".2e")                                      # Conversion en nombre scientifique.
    print(f"Case {case} = {grains_de_riz} grains de riz - notation scientifique = {grains_scientifique} grains de riz.")  
    grains_de_riz *= 2                                                                      # Le riz par case fois 2 chaque tour.
    case += 1                                                                               # L'ajout d'une case a chaque tour.
total_grains = (2**64) - 1
print(f"Total de grains sur l'échiquier : {total_grains:e} grains")
