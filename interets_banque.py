# Calcule d'intérêts accumulés par année (en 20 ans).

capital = 100                               # Ma variable avec ma somme de base.
taux = 4.3 / 100                            # Ma variable avec le taux de 4.5%.
interets = capital * taux                   # Ma variable avec les intèrêts sur la somme de base.
capital_annee = capital + interets          # Ma variable avec mon capital par année.
capital_total = capital_annee * 20          # Ma variable avec mon capital total sur 20 ans.
print(f"Avec un capital de base de {capital}€ plus 4,3% d'intérêts de la banque qui fait {interets:.2f}€, je gagne {capital_annee:.2f}€ par année, et sur 20 ans j'aurais {capital_total:.2f}€")    

# .2f demande de s'arreter à la 2 ieme décimale.