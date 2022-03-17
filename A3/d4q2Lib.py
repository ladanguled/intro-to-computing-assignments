#Devoir 4
#Numero etudiant: 300021664
#Nom: Ladan Guled
#Nom Partenaire: Tenimba Coulibaly


def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
    # a completer

   i = 0
   while i < len(tab):  # on utilise deux boucles while (une dans l'autre) pour avoir accès a toutes les éléments de la matrice
      j = 0
      while j < len(tab[i]):
         tab[i][j] = '-'  # on toutes les élément de la matrice par '-'
         j = j + 1
      i = i + 1
      
    # retourne rien

      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    # a completer
    res = False   # on initialize une variable booléenne qui est d'abord égale à False
    cols = testCols(tab)    # on appelle la fonction testCols et elle retourne dans une variable cols
    lignes = testLignes(tab)    # on appelle la fonction testLignes, ensuite elle retourne dans une variable lignes
    diags = testDiags(tab)   # on appelle, enfin, la fonction testDiags et elle retourne dans une variable diqgs
    if cols=='X' or lignes=='X' or diags=='X':    # si le if statement retourne une des trois fonctions est 'X', le joueur X gagne
       print('Joueur X a gagné!')  # ceci affiche un message qui indique le joueur gagnant
       res = True     # on change la variable booléenne a True de la variable res qu'on a crée auparavant
    elif cols=='O' or lignes=='O' or diags=='O':     # si le elif statement retourne une des trois fonctions est 'O', le joueur O gagne
       print('Joueur O a gagné!')    # ceci affiche un message
       res = True    # on change la variable booléenne a True de la variable res qu'on a crée auparavant 
    elif testMatchNul(tab)==True:    # on fait appelle la fonction testMatchNul,le match est nul si elle retourne True 
       print ('Match Nul')   # ceci affiche un message
       res = True     # on change la variable booléenne a True de la variable res qu'on a crée auparavant
    return res    # la fonction verifieGagner retourne la variable res

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   res = '-'   # on crée une variable res 
   i = 0
   while i < len(tab):  # on utilise deux boucles while pour avoir accès a toutes les éléments de la matrice 
      j = 0
      while j < len(tab[i])-2:  
         if tab[i][j]==tab[i][j+1]==tab[i][j+2] and tab[i][j]=='X': # on compare tous les éléments d'une ligne 
            res = 'X' # si ils sont égales à 'X'ca affecte la variable res 'X'
         elif tab[i][j]==tab[i][j+1]==tab[i][j+2] and tab[i][j]=='O': # on compare tous les éléments d'une ligne 
            res = 'O' # si ils sont égales à 'O' ca affecte la variable res 'O'
         j = j + 1
      i = i + 1
   return res #retourne res

  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   res = '-' # on fabrique une variable res qui est égale d'abord à '-'
   j = 0
   while j < len(tab[0]): # on utilise deux boucles while pour avoir accès a toutes les éléments de la matrice 
      i = 0
      while i < len(tab)-2:
         if (tab[i][j] == tab[i+1][j] == tab[i+2][j]) and tab[i][j]=='X': #on compare les éléments des colonnes 
            res = 'X'  # si ils sont égales à 'X', on affecte la variable res qui devient 'X'
         elif (tab[i][j] == tab[i+1][j] == tab[i+2][j]) and tab[i][j]=='O':
            res = 'O' # si ils sont égales à 'O', on affecte la variable res qui devient 'O'
         i = i + 1
      j = j + 1
   return res  #on retourne la variable res qui est égale soit a '-', 'X' ou 'O'

   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   res = '-'  # on crée une variable res qui est initialement égale à '-'
   i = 0  # on initialise i qui va servir comme notre index

   # grace au if statement, on compare les éléments diagonales de la matrice (pour la diagonale, i qui indique la ligne est égale à i qui indique la colonne) 
   if ((tab[i][i]==tab[i+1][i+1]==tab[i+2][i+2]) and (tab[i][i]=='X')) or ((tab[i][len(tab[i])-1]==tab[i+1][i+1]==tab[len(tab)-1][i]) and tab[i+1][i+1]=='X'): 
      res = 'X'     #  si tous les éléments d'une des diagonales sont égales à 'X', la variable res prend la valeur de 'X'  
   elif ((tab[i][i]==tab[i+1][i+1]==tab[i+2][i+2]) and (tab[i][i]=='X')) or ((tab[i][len(tab[i])-1]==tab[i+1][i+1]==tab[len(tab)-1][i]) and tab[i+1][i+1]=='O'):
      res = 'O'    # si tous les éléments d'une des 2 diagonales sont égales à 'O' alors la variable res prend la valeur 'O'
   return res   # la fonction retourne res

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   res = True   # on fabrique la variable res qui sera initialement égale à True
   i = 0
   while i < len(tab) and res: # on utilise deux boucles while pour avoir accès a toutes les éléments de la matrice  (une des conditions de la boucle est que res doit etre égale à True)
      j = 0
      while j < len(tab[i]) and res:
         if tab[i][j] == '-':   # si au moins un élément de la matrice est égale à '-' alors la variable res prend la valeur booléenne False ensuite les deux while boucles while s'arretent
            res = False
         j = j + 1
      i = i + 1
   return res  #testMatchNul retourne soit True ou False en fonction de la variable res

