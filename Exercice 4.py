b100 = 0
b50 = 0
b10 = 0
P2 =0
P1 = 0



n = int(input("Valeur ? :"))
b100 = n / 100
n = n %100
b50 = n /50
n = n%50
b10 = n/10
n = n%10
P2 = n/2
P1 = n%2

print(f"{n}"+ "c'est donc {b100} + billet de 100" )