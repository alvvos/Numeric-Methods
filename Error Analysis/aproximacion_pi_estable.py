from math import sqrt, pi
iter = 50

yn = 2.0 # y1,  mitad del perímetro de un polígono de 2 lados ins. circ. r=1 
print(f"n \t y_n")
print(f"1 \t {yn}")
for n in range(1, iter):
    yn = sqrt(2.0/(1.0 + sqrt(1.0 - (2.0 **(-n)*yn)**2))) * yn
    print(f"{n+1} \t {yn}")

print(pi)