# Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères.
# Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »


chaine = "gaston"                   # Ma chaine de base.
chaine_etoile = ""                  # Ma chain_etoile vide.
tour = 0                            # Ma variable pour les tours.

while tour < len(chaine):           # Ma boucle qui tourne temps que je n'ai pas atteint le nombre de caractère dans chaine.
    chaine_etoile += chaine[tour]   # J'assigne à chaque tour une lettre de plus.
    if tour < len(chaine) - 1:      # Si j'atteint le dernier caractere.
        chaine_etoile += "*"        # J'ajoute une étoile dans ma chaine_etoile.
    tour += 1                       # J'augmente de 1 pour passer au tour suivant.
    
print(chaine_etoile, end = "")      # J'utilise end pour rester sur ma ligne.