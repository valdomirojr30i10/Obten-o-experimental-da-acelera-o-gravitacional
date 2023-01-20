#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 00:52:41 2020

@author: valdomiro
"""

#Obtem os valores calculados atraves da redução de dados experimentais
# e converte os valores do arquivo para uma lista de numeros float
def ler_dados(a):
    #abre arquivo em um endereço 'a' em modo leitura
    dados = open(a,"r")
    
    #cria as listas que serão utilizadas nessa função
    alturas = []
    tempos = []
    desvios = []
    
    #atribui para as listas alturas, tempos e desvios, os valores adquiridos
    # pelo programa 'reducao_dados_experimentais.py'
    for i in range(5):
        k = dados.readline()
        
        # remove textos e unidades de medidas dos dados, deixando apenas 
        # valores numéricos separados por um espaço: ' ',
        # facilitando o tratamento dos dados
        k = k.replace("altura: ","")
        k = k.replace("  |  tempo: ","")
        k = k.replace("  |  desvio padrão: ","")
        k = k.replace("m"," ")
        k = k.replace("s"," ")
        
        alturas.append(k[0]+k[1]+k[2])
        tempos.append(k[4]+k[5]+k[6]+k[7])
        desvios.append(k[9]+k[10]+k[11]+k[12])
       
    #efetua a conversão dos valores das listas de tipo char para tipo float
    alturas =  [float(i) for i in alturas]
    tempos  =  [float(i) for i in  tempos]
    desvios =  [float(i) for i in desvios]
    
    #fecha o arquivo aberto para leitura e retorna as listas
    dados.close()
    return [alturas,tempos,desvios]
