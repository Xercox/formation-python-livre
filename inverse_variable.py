#Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant.
#Ainsi par exemple, « zorglub » deviendra « bulgroz ».

chaine = "zorglub"
inverse = chaine[::-1]

print(inverse)

texte = "formation python"
chaine_inversee = ""

index = len(texte) - 1  # On commence à la fin de la chaîne

while index >= 0:
    chaine_inversee += texte[index]
    index -= 1  # On recule d’un caractère

print(chaine_inversee)
