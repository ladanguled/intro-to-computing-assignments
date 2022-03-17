import random#Import des valeurs aleatoires

def effectuezTest(operation):#la fonction definit pour effectuez des multiplications et des additions
    resultat = False
    numero1 = random.randint(0,9)
    numero2 = random.randint(0,9)
    if operation == 0:#Commence intialement par 0
        reponse = int(input(str(numero1) + " + " + str(numero2) + " = "))
        somme = numero1 + numero2
        if somme == reponse :
            resultat = True#Ceci permet de passer a la question suivante
        else: #Cela permet d'imprimer que la reponse est fausse et donne la bonne reponse
            print("Incorrect - la reponse est", somme)
    else:
        reponse = int(input(str(numero1) + " * " + str(numero2) + " = "))
        multi = numero1 * numero2
        if(multi == reponse) :
            resultat = True#permet de passer a la question suivante
        else :
                print("Incorrect - la reponse est", multi)
    return resultat# Affiche le nombre total de bonne reponse et les commentaires

reponsesCorrectes = 0
print("Ce logiciel va effectuez un test avec 10 questions ");#Cela affiche la question  
for compteur in range(10):
    operation = random.randint(0,1)
    if effectuezTest(operation) == True: #Fait appel a la fonction
        reponsesCorrectes += 1
print(reponsesCorrectes, "reponses correctes.")
if reponsesCorrectes <= 6 :
    print("Demandez à votre enseignant(e) pour de l'aide")
else :
    print("Felicitations!")
    
