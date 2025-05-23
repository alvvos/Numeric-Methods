import numpy as np

f_estable = lambda x: np.sin(x)**2 / (x**2 * (1 + np.cos(x)))
xi = (1.e-5, 1.e-6, 1.e-7, 1.e-8, 1.e-9, 1.e-10, 1.e-11)
for x in xi:
    print(f'f_estable({x}) = {f_estable(x)}')