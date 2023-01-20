import numpy as np
import ajuste
import grafico
import abre_arquivo

lista = abre_arquivo.ler_dados("redução_dados_experimentais.txt")

# atribui alturas e tempos para as listas x e y:
h,t,d = lista

# Utilizando o processo de encontrar a equação linear:
# Após ajustar a função "t = (2*h/g)**(1/2)", foram obtidos:
# Y = ln(t**2)  
# x = ln(h)
# a0 = ln(2)-ln(g)
# a1 = 1

Y = [np.log(i**2) for i in t]
x = [np.log(i) for i in h]

# Aplicando a função ajuste e encontrando os valores experimentais de a0 e a1
a0,a1 = ajuste.reta(x,Y)
g = 2/np.e**a0

print("a1 teorico: 1, a1 encontrado: ",a1)
print("g encontrado: ", g)

grafico.plot_errorbar(lista,g)
