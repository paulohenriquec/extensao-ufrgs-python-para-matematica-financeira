#%%
dados = [2,3,4,-5]
#%%
print(dados[0])
print(dados[2])
print(dados[-1])
#%%
#Tamanho da lista
len(dados)
#%%
lista2 = ['Ações', 'títulos', 'CDB', 'FII', 'ETF']
print(lista2)
print(lista2[0:3])
print(lista2[0:5:2]) #Imprime a lista de 2 em 2
print(lista2[::-1]) #Imprime a lista na ordem inversa
#%%
"dolar" in lista2
"Ações" in lista2
#%%
lista2[0] = 'Dólar'
lista2[0:3] = ['Reais', 'Ouro', 'Poupança']
#%%
lista2.append('Euro')
lista2
#%%
lista2.extend(['Bitcoin', 'Ethereum', 'Yen'])
#%%
lista2.sort(key=str.casefold, reverse=True) #Key = str.casefold desconsidera o case sensitive
lista2
#%%
lista2.remove('Bitcoin')
#%%
lista2.index('Reais')
#%%
lista2.insert(3, 'Outros')
#%%
lista2.clear()
#%%
list = [1,2,3,2]
list.remove(2)
list