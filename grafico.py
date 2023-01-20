#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 00:27:16 2020

@author: valdomiro
"""
import matplotlib.pyplot as plt

# função similar ao np.linspace da biblioteca numpy
def linspace(inicio,fim,tamanho):
    lista = []
    assert(inicio < fim), "o primeiro valor deve ser menor que o final"
    k = inicio
    for i in range(tamanho):
        lista.append(k)
        k+=(fim-inicio)/(tamanho-1)
    return lista
'''def plot_errorbar(g,x,y,d): 
    x = linspace(0.2,2.2,10)
    y = [(2*i/g)**(1/2) for i in x]

    plt.plot(x, y)
    plt.suptitle("Grafico Altura X Tempo de queda", fontsize=18)
    plt.errorbar(x,y, yerr = d, fmt = 'ro',)
    plt.axis([1.0, 2.2, 0.4, 0.8])   
    plt.grid(True)
    plt.xlabel('Altura (m)')
    plt.ylabel('Tempo (s)')
    plt.show()
    plt.savefig('altura x tempo.png')
    '''
def plot_errorbar(lista,g_experimental): 
    g = 9.81
    x = linspace(0.2,2.2,10)

    # aplicando a formula 'y = (2*h/g)**(1/2)' em diversos pontos de h: 
    y = [((2*i)/g)**(1/2) for i in x]
    y_experimental = [(2*i/g_experimental)**(1/2) for i in x]
    
    plt.plot(x, y, label='g = 9.81 m/s²')
    plt.plot(x,y_experimental, label='g = {:.2f}m/s²'.format(g_experimental))
    plt.legend(loc=2)
    plt.suptitle("Grafico Altura X Tempo de queda", fontsize=18)
    plt.errorbar(lista[0],lista[1], yerr = lista[2], fmt = 'ro',)
    plt.axis([1.0, 2.2, 0.4, 0.8])   
    plt.grid(True)
    plt.xlabel('Altura (m)')
    plt.ylabel('Tempo (s)')
    plt.show()
    plt.savefig('altura x tempo.png')