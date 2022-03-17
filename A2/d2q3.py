import random#Pour avoir des valeurs aleatoires
def effectuezTest(operation):#Pour effectuez un test de 10 questions
    compteur = 0#Les questions commencent de zero
    reponsesCorrectes = 0
    if operation == 0:
        print("SVP donnez les reponses aux additions suivants:")#cela la partie est pour les addtions
        for i in range(10):#Deux entiers de 0 a 9
            numero1 = random.randint(0,9)
            numero2 = random.randint(0,9)
            reponse = int(input(str(numero1) + " + " + str(numero2) + " = "))#str permet de convertir le nombre en string 
            somme = numero1 + numero2
            if somme == reponse :
                reponsesCorrectes += 1#ceci permet d'evaluer le resultat
            else:
                print("Incorrect la reponse est", somme)
    else:
        print("SVP donnez les reponses aux multiplications suivantes:")#cela est la partie pour les multiplications
        for compteur in range(10):
            numero1 = random.randint(0,9)
            numero2 = random.randrange(0,9)
            reponse = int(input(str(numero1) + " * " + str(numero2) + " = "))
            multi = numero1 * numero2
            if(multi == reponse) :
                reponsesCorrectes += 1
            else :
                print("Incorrect la reponse est", multi)
    return reponsesCorrectes

reponsesCorrectes = 0
print("Ce logiciel va effectuez un test avec 10 questions ");
operation = int(input("SVP choisiser l'operation 0) Addition 1) Multiplication (0 ou 1): "))#Ceci permet de poser la question et choisir soit l'addtion ou la multiplication

reponsesCorrectes = effectuezTest(operation) #Fait appel a la fonction
print(reponsesCorrectes, "Reponses Correctes.")
if reponsesCorrectes <= 6 :#s'il y a plus que 6 reponses fautes, affiche le message 
    print("Demandez a votre enseignant(e) pour de l'aide.")
else :#s'il y a plus que 7 bonnes reponses, affiche le message 
        print("Felicaitations!")
