#Ceci permet d'importer la fonction
def BMI(p,t):
    bmi = (p / (t** 2)) #Ceci permet de calculer le BMI
    #Le "if permet d'affichez le bon message par rapport au resultat donner
    if bmi < 18.5:
        print("Votre BMI est",bmi)
        print("Maigeur")
    if bmi >= 18.5 and bmi < 25:
        print("Votre BMI est", bmi)
        print("Poids ideal")
    if bmi >= 25 and bmi< 30:
        print("Votre BMI est", bmi)
        print("Surpoids")
    if bmi > 30:
        print("Votre BMI est", bmi)
        print("Obesite")

#Demandez a l'utilisateur d'entrez leur taille et poids
poids = float(input("SVP entrez votre poids en kilogrammes:"))
taille = float(input("SVP entrez votre taille en metres:"))
BMI(poids, taille) #Faire appel a la fonction 
              
