# Conversion entre Celsius et Fahrenheit

choix = input ("Taper 'celsius' ou 'fahrenheit' en fonction de la conversion désiré : ").strip().lower()  # Ma variante demande à l'utilisateur de faire un choix. 

if choix == "celsius":                                                                                    # Si le choix est en celsius.
        degres_celsius = float(input ("Entrer la température en degrés Celsius : "))                      # Transforme en float les celsius et fait une demande.
        degres_fahrenheit = (degres_celsius * 9 / 5) + 32                                                 # Transforme en Fahrenheit les celsius.
        print(f"{degres_celsius}°C = {round(degres_fahrenheit, 2)}°F")  
elif choix == "fahrenheit":                                                                               # Sinon si le choix est en fahrenheit.
        degres_fahrenheit = float(input ("Entrer la température en degrés Fahrenheit : "))                # Transforme en float les fahrenheits et fait une demande.
        degres_celsius = (degres_fahrenheit -32) * 5 / 9                                                  # Transforme en celsius les Fahrenheit.
        print(f"{degres_fahrenheit}°F = {round(degres_celsius, 2)}°C")
else:                                                                                                     # Sinon.
        print("Choix non valide. Veuillez taper 'celsius' ou 'fahrenheit'.")                               