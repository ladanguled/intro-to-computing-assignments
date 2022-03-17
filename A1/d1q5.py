import math
#exercise 5
#a
def anneesEnSecondes(annees):
    "Transforme les annees siderales en secondes"
    n_secondes_annee_siderale = (n_annee_lumiere * 31557600)
    return n_secondes_annee_siderale

n_annee_lumiere = float(input("Entrez un nombre d'année-lumière:"))
nombre_secondes_annee_siderale = anneesEnSecondes(n_annee_lumiere)
print ("Le nombre de secondes-lumière est", nombre_secondes_annee_siderale)   


#b)
def secondesLumiereEnKm(distance):
    "Transforme les secondes lumieres en km"
    km = n_secondes_lumieres * (3.3356410 * math.pow(10, -6))
    return km

n_secondes_lumieres = float(input("Entrez les secondes lumieres:"))
km = secondesLumiereEnKm(n_secondes_lumieres)
print ("La distance est:", km, "km.") 

#c)
def distanceEntreEtoiles(distance):
    "Calculez la distance entre la premiere etoile et la deuxieme etoile"

premiere_etoile = float(input("Entrez la distance de la premiere etoile, en annees-lumieres:"))
deuxieme_etoile = float(input("Entrez la distance de la deuxieme etoile, en annees-lumieres:"))

d1 = premiere_etoile * 31557600
d2 = deuxieme_etoile * 31557600

km1 = (d1 + d2) * (31536000 * math.pow(10, -6))                  
km = distanceEntreEtoiles(km1)

print("La distance entre les deux etoiles est", km1, "km.")

#pour lire a partir du clavier, il faut faire distanceEntreEtoiles("entrez un valeur") dans la partie entrez une valeur, il faut mettre la premiere distance (premiere etoile) aditionner avec la deuxieme distance.
#apres il faut multiplier les deux avec (31536000 * math.pow(10, -6)) ce qui va donner la valeur en km 
