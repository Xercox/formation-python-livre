# Écrivez un programme qui convertit un nombre entier de secondes fourni au départ en un
# nombre d’années, de mois, de jours, de minutes et de secondes (utilisez l’opérateur modulo : %).

total_secondes = 25905840
reste = 0

annees = total_secondes // ((365 * 24 * 60 * 60)) # On lui demande de calculé le nombre de jour * heure * minute * seconde pour calculer le nombre d'année
reste = total_secondes % (365 * 24 * 60 * 60)     # On lui demande ce qu'il va rester une fois les années décompté 

mois = reste // (30 * 24 * 60 * 60)               # On lui demande de calculé le nombre de jour * heure * minute * seconde pour calculer le nombre de mois
reste =  reste % (30 * 24 * 60 * 60)              # On lui demande ce qu'il va rester une fois les mois décompté 

jours = reste // (24 * 60 * 60)                   # On lui demande de calculé le nombre d'heure * minute * seconde pour calculer le nombre de jours
reste = reste % (24 * 60 * 60)                    # On lui demande ce qu'il va rester une fois les jours décompté

heures = reste // (60 * 60)                       # On lui demande de calculé le nombre de minute * seconde pour calculer le nombre d'heure'                   
reste = reste % (60 * 60)                         # On lui demande ce qu'il va rester une fois les heures décompté

minutes = reste // 60                             # On lui demande de calculé le nombre de seconde pour calculer le nombre de minute'

secondes = reste % 60                             # On lui demande ce qu'il va rester une fois les minutes décompté

print(f"{total_secondes} secondes = {annees} année(s) {mois} mois {jours} jour(s) et {heures}h{minutes}, {secondes} s")