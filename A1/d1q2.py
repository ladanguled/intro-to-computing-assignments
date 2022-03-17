# exercise 2
dollars = float(input("Entrez le montant en dollars:"))

if dollars <= 0:
        print ("Erreur, les dollars et sous sont positives")
else:
        Vingtcinq_Cents = dollars*100 // 25
        Dix_cents = (dollars*100 % 25) // 10
        Cinq_cents = dollars*100 % 25 % 10 // 5
        Un_cent = dollars*100 % 5

resultat = (Vingtcinq_Cents + Dix_cents + Cinq_cents + Un_cent)

print ("Le nombre minimal de pieces que le cassier peut rendre est:", resultat)
        


