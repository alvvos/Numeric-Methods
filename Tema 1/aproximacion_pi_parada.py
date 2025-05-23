from math import sqrt, pi
TOL = 1.0e-15
MAXITER = 100

iter = 0 # n-1
yn = 2.0 # y1,  mitad del perímetro de un polígono de 2 lados ins. circ. r=1 
print(f"n \t y_n")
print(f"1 \t {yn}")
error = TOL + 1

while error > TOL and iter < MAXITER:
    iter += 1
    ynext = sqrt(2.0/(1.0 + sqrt(1.0 - (2.0**(-iter)*yn)**2))) * yn
    error = abs(ynext-yn)
    yn = ynext
    print(f"{iter+1} \t {yn}")

print(pi)