#%%
import numpy as np
import matplotlib.pyplot as plt
from math import cos, exp
import statistics as st
from scipy.stats import norm

x = [4,2,1,0,4,10,9,8,11,14]

plt.hist(x, bins = 5, density=True)
#%%
media = st.mean(x)
desvio = st.stdev(x)

xmin, xmax = plt.xlim()

eixox = np.linspace(xmin, xmax, 100)
eixoy = norm.pdf(eixox, media, desvio)

plt.plot(eixox, eixoy)