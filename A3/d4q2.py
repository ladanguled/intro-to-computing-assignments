#Devoir 4
#Numero etudiant: 300021664
#Nom: Ladan Guled
#Nom Partenaire: Tenimba Coulibaly


from d4q2Lib import *
    
def afficheTableau (tab):
    '''
    (list) -> None
    Affiche le tableau de jeu
    Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    Le format est: 
        0 1 2
      0 - - O
      1 - X -
      2 - - X
    '''
    print("   ", end="")
    col = 0
    while col < len(tab): 
      print(col, end="  ")
      col += 1
    print()  
    row = 0  
    while row < len(tab):  
      print(row, end="")
      col = 0
      while col < len(tab[row]): 
        print(" ",tab[row][col], end="")
        col += 1
      print()
      row += 1

def joue (tab, joueur):
    '''
    (list, str) -> None
    Joue une étape de jeu
    Preconditions: tab is a reference to the n x n tab containing '-', 'X' and 'O'
    Le joueur est X ou O
    tab est modifié (un element est changé)
    '''               
    
    valid = False
                 
    while not valid:   
        place = [-1,-1] # ceci est pour fabriquer un tableau avec deux éléments
        while not((0 <= place[0] < len(tab)) and (0 <= place[1] < len(tab))):
          print ("Joueur ",joueur, end="")
          print(", SVP donner la ligne et la colonne de 0 à", (len(tab)-1), ": ")
          place[0] = int(input("Ligne: ")) # 
          place[1] = int(input("Colonne: "))
        #cela trouve une position qui n’est pas occupée ce qui contient '-‘             
        if tab[place[0]][place[1]] != '-':
          print("La position", place[0], place[1], "est occupée");
          valid = False
        else:
          valid = True             
          # cela met le joueur dans la matrice 
          tab[place[0]][place[1]] = joueur 
    # il n'y a pas de resultat
  

# Créer le tableau pour le jeu 
tableau = [['-','-','-'],['-','-','-'],['-','-','-']] # la matrice utilisé dans le programme
    
reponse = input("Commence un jeu (O ou N): ");    
while reponse == 'o' or reponse == 'O': 
      effaceTableau(tableau)  # prepare le tableau pour le jeu
      gagnant = False  # initialise la variable gagnant 
      while not gagnant: 
        afficheTableau(tableau) # affiche le tableau pour le jeu
        joue(tableau,'X')  # demande au joueur X de jouer
        gagnant = verifieGagner(tableau)  # verifie si le joueur a gagné
        if not gagnant: 
          # pas de gagnant alors l’autre joueur peut jouer
          afficheTableau(tableau) # affiche le tableau pour le jeu
          joue(tableau,'O')  # demande au joueur O de jouer
          gagnant = verifieGagner(tableau)  # verifie s'il a gagné
          
      afficheTableau(tableau) #  affiche le tableau pour le jeu
      reponse = input("Commence un jeu (O ou N): ") # commence un nouveau jeu
