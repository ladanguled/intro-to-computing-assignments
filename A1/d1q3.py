#exercise 3
def convertEnKilos(lb, once):
    kg1 = lb / 2.2046
    return kg1

    lb = int(input("Entrez le nombre de livres: "))
    n_kg1 = lb_en_kg1(lb)   
                
    print(lb, "livres est équivalent à", n_kg1, "kilos.")

    kg2 = once * 0.02834952
    return kg2
                 
    once = float(input("Entrez le nombre d'once: "))
    n_kg2 = once_en_kg2(n_once)

    print(n_once, "onces est équivalent à", n_kg2, "kilos.")

    n_kg = n_kg1 + n_kg2

    print(lb, "livres et",once,"onces équivalent à", n_kg, "kilos.")

#J'ai compris que la question veut qu'on utilise la fonction convertEnKilos dans le Shell et ont imprime la valeur combinée en kg 
