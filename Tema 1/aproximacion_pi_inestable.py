from math import sqrt
ITER = 50

yn = 2.0 # y1,  mitad del perímetro de un polígono de 2 lados ins. circ. r=1 
print(f"n \t y_n")
print(f"1 \t {yn}")
for n in range(1, ITER):
    yn = 2.0**(n+1)*sqrt(0.5*(1.0 - sqrt(1.0 - (2.0 **(-n)*yn)**2)))
    print(f"{n+1} \t {yn}")