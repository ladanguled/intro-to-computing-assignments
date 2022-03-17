#Devoir 4
#Numero etudiant: 300021664
#Nom: Ladan Guled
#Nom Partenaire: Tenimba Coulibaly


def ajoute(M):
    '''matrice ---> matrice'''
    M2 = [[i+1 for i in j] for j in M] #crée la nouvelle matrice en incrémentant par valeur de 1 pour chaque valeur de liste (M[j][i])
    return M2 # retourne la nouvelle matrice

def ajoute_V2(M2):
    '''matrice ---> matrice'''
    M3 = [[i+1 for i in j] for j in M2] #ajoute valeur de 1 dans chaque element da la matrice M2
    return M3 # retourne la nouvelle matrice 

        

print("Entrez les nombres avec des espaces entre les colonnes.")  #ceci est pour l’usager d’introduire toutes les valeurs de la rangée 
print("Une rangee par ligne, et une ligne vide a la fin.") #imprime les directions de la matrice
M = [] #Matrice vide 
while True:
    ligne = input() #après chaque rangée, passe à une nouvelle ligne
    if not ligne: break #le while loop se s'arrete si la ligne est vide 
    valeurs = ligne.split() # separe les cols qui est separer par une espace
    rangee = [int(val) for val in valeurs] # fait les rangees
    M.append(rangee) # ajoute la rangee a la matrice 
    
    
w = M # change la matrice 'M' a la variable 'w'
x = ajoute(w) # fait appelle la fonction ajoute avec la matrice est l'affecte avec la variable x
y = ajoute_V2(x)#fait appelle la fonction ajoute_V2 avec la matrice est l'affecte avec la variable y
z = x # affecte la matrice incrementer à la variable z 
print ("La matrice est: \n",w)# imprime la matrice initiale
print('Apres exécution de la fonction ajoute, la matrice est:\n',x)# imprime la matrice incrementer 
print('Une nouvelle matrice créée avec ajoute_V2:\n',y)#imprime la deuxieme matrice par ajoute_V2
print('Apres exécution de la fonction ajoute_V2, la matrice initiale est:\n',z)#imprime la matrice avant l'incrementation

