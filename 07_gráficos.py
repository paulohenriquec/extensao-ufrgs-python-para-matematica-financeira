#%%
import numpy as np
import matplotlib.pyplot as plt
from math import cos, exp

n = int(input('Número de pontos a serem impressos = '))

x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

for i in range(n):
    x[i] = i*0.1
    y[i] = exp(-0.1*x[i])*cos(x[i])
    z[i] = cos(x[i]) + 1

plt.plot(x,y, '-b', x, z, '-r')
plt.title('Dois gráficos')
