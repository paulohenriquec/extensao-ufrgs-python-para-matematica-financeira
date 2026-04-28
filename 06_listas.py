#%%
import numpy as np

n = int(input("Número de termos= "))

x = np.zeros(n)
y = np.zeros(n)

soma = 0

for i in range(n):
    x[i] = float(input('x = '))
    y[i] = 10 * x[i]
    soma = soma + x[i] + y[i]

print(f"Soma das coordenadas de x e y = {soma}")
print(f"Soma dos elementos de x = {x.sum()}")
print(f"Média dos elementos de x = {x.mean()}")
print(f'Desvio padrão de x = {x.std()}')
print(f'Valor mínimo de x = {x.min()}')
print(f'Valor máximo de x = {x.max()}')
print(f'Posição do menor valor de x = {x.argmin()}')
print(f'Posição do maior valor de x = {x.argmax()}')