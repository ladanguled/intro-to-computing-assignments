#D'abord il faut afficher les entiers
def affiche(a,b):
    for i in range (a, b+1): #Ceci permet d'afficher des valeurs de a jusqu'a b (b+1) permet d'inclure le b
        print(i)

a = int(input("SVP donner la valeur de a:"))
b = int(input("SVP donner la valeur de b:"))
affiche(a,b) #Ceci fait appel a la fonction, qui va afficher le resultat 
