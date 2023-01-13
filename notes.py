n =0
no =0
coeff =0
Somme = 0
Somme_coeff = 0
for i in range(5):
    n = input(f"Veuillez entrer la note du module {i} et le coefficient\ncorrespondant:")
    Recherche = n.split(" ")
    no = float(Recherche[0])
    coeff = float(Recherche[1])
    Somme = Somme + (no * coeff)
    Somme_coeff = Somme_coeff + coeff
    moy = Somme / Somme_coeff
print(moy)

if moy > 10 and float(Recherche[0])>8:
    print("L'étudiant est admis !")

else:
    print("L'étudiant n'est pas admis")