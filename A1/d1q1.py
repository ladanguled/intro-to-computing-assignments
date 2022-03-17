# exercise 1 
def lb_en_kg1(lb):
  "Transforme des livres en kilo"
  kg = lb / 2.2046 
  return kg

n_lb = int(input("Entrez le nombre de livres: "))
n_kg1 = lb_en_kg1(n_lb)   
                
print(n_lb, "livres est équivalent à", n_kg1, "kilos.")


def once_en_kg2(once):
  "Transforme des onces en kilo"
  kg = once * 0.02834952
  return kg
                 
n_once = float(input("Entrez le nombre d'once: "))
n_kg2 = once_en_kg2(n_once)

print(n_once, "onces est équivalent à", n_kg2, "kilos.")

n_kg = n_kg1 + n_kg2

print(n_lb, "livres et",n_once,"onces équivalent à", n_kg, "kilos.")

