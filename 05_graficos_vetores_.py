#%%
import numpy as np
import matplotlib.pyplot as mp

#%%
x = np.arange(-10,10)
#%%
y = 3*x**2-1
#%%
mp.plot(x,y)
mp.xlabel('Eixo X')
mp.ylabel("Eixo y")
mp.title('$y=3x^2-1$')
mp.grid()
mp.savefig('fig1.jpg')
#%%
y=2*x
z=x**5+7
w=-2*x**2-1
#%%
mp.subplot(311)
mp.plot(x,y)
mp.title('Mais gráficos')
mp.grid()

mp.subplot(312)
mp.plot(x,z)
mp.grid()

mp.subplot(313)
mp.plot(x,w)
mp.grid()

mp.savefig('fig2.jpg')
#%%
lista = [10,2,-4,5,1,15,7]
vetor = np.array(lista)
#%%
ret = (vetor[1:7]- vetor[0:6])/vetor[0:6]
#%%
mp.plot(ret)
mp.title('Retorno financeiro')
mp.grid()
mp.savefig('fig3.jpg')
#%%
x = np.array([10,20,30])
x.mean()