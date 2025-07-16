# Écrivez un script qui compte le nombre d’occurrences du caractère « e » dans une chaîne.

chaine = "Le petit renard cherche une belle cachette verte."    # Ma cahine de caractère.
caractere_e = 0                                                 # Mon nombre de caractère "e". 
tour = 0                                                        # Mon indicateur de tour.

while tour < (len(chaine)):                                     # Ma boucle while qui va faire le même nombre de tour que de caratère.
    if chaine[tour] == "e":                                     # Si ma chaine sur le tour est strictement égale a "e".
        caractere_e += 1                                        # Ajoute + 1 à mon compteur de caractere_e
    tour += 1                                                   # Augmente de 1 le compteur de tour jusqu'au nombre de caractère.

print(caractere_e)