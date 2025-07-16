# Vérifier si la chaine de caractère contient (e) ou non.

chaine = input("Dit moi une phrase et je te dirais si elle contient 'e' ou non.\n")           # Demande à l'aide d'input une phrase à la personne \n fait sauter à la ligne.

if "e" in chaine:                                                                             # Si il y a "e" dans la chaine.
    print("Cette phrase contient la lettre (e).")
else:                                                                                         # Sinon 
    print("Cette phrase ne contient pas la lettre (e).")
