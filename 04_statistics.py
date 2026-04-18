#%%
import statistics as st

x = [10,9,2,3,11,20,20]

print(f'Média: {st.mean(x)}')
print(f'Mediana: {st.median(x)}')
print(f'Moda= {st.mode(x)}')
print(f'Desvio padrão: {st.stdev(x)}')
print(f'Média Harmônica: {st.harmonic_mean(x)}')
print(f'Variância: {st.variance(x)}')