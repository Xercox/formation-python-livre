# Écrivez un programme qui calcule le volume d’un parallélépipède rectangle dont sont fournis
# au départ la largeur, la hauteur et la profondeur.
def format_nombre(nombre):                              # Si le nombre n'a pas de décimal l'afficher en int et pas en float
    if nombre == int(nombre):                           # On vérifie si le nombre est un entier.
        return str(int(nombre))                         # Si sans virgule il est convertit en int puis en chaine pour l'afficher proprement.
    else:
        return str(nombre)                              # Sinon si décimal on le convertis en chaine sans iren modifier.

hauteur = float(input("Quelle est la hauteur ?\n"))     # je j'autorise l'entrée en float et demande a l'utilisateur un nombre pour la hauteur.
longueur = float(input("Quelle est la longueur ?\n"))   # "                                                                       " la longueur.
largeur = float(input("Quelle est la largeur ?\n"))     # "                                                                       " la largeur.

print(f"Le volume de mon parallélépipède est de : {format_nombre(hauteur)} x {format_nombre(longueur)} x {format_nombre(largeur)} = {format_nombre(longueur * largeur * hauteur)}.")
