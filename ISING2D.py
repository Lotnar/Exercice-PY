# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:28:50 2018

@author: Abraão
"""

import numpy as np
from numpy.random import rand

#gera uma configuração de spin aleatoria para as condiçoes iniciais
def initialstate(L):   
    state = np.random.randint(3, size=(L,L))-1
    return state


#Passo de Monte Carlo usando o algoritimo Metropolis
def mcmove(config, beta):
    for i in range(L):  
        for j in range(L):
                a = np.random.randint(0, L)
                b = np.random.randint(0, L)
                s =  config[a, b]
                nb = config[(a+1)%L,b] + config[a,(b+1)%L] + config[(a-1)%L,b] + config[a,(b-1)%L] + config[a,(b)%L] + config[(a)%L,b]
                cost = 2*s*nb
                if cost < 0:
                    s *= -1
                elif rand() < np.exp(-cost*beta):
                    s *= -1
                config[a, b] = s
    return config

 #energia de uma configuração, onde os comandos range determina o alcançe e len retorna um valor da config
def calcEnergy(config):
    energy = 0
    # o i e o j, são os subindices da hamiltoniana
    for i in range(len(config)):
        for j in range(len(config)):
            S = config[i,j]   # S  representa os spin lembrando que pode ser +1 e -1, como o sistema não é ferromagnetico esses valores não serão ordenados
            nb = config[(i+1)%L, j] + config[i,(j+1)%L] + config[(i-1)%L, j] + config[i,(j-1)%L] + config[i,(j)%L] + config[(i)%L,j] #Representa as possibilidades spin esquerda, direita, cima e baixo
            energy += -nb*S
    return energy/4.

#Magnetização de uma configuração
def calcMag(config):
    mag = np.sum(config)
    return mag
##############################################################################
# Parametros responsaveis pelo tamanho do sistema, ou seja, variação deles afeta no tamanho do sistema.
nt = 2**8        # numero de pontos de temperatura
L = 2**4        # tamanho da lattice, L x L
eqSteps = 2**10       # numero de passos de MC para alcançar o equilibrio
mcSteps = 2**10       # numero de passos de MC para o calculo
#No equilibrio, a temperatura será comparada com a temperatura critica e com base nisso sabemos se o sistema está magnetizado ou não.
n1, n2  = 1.0/(mcSteps*L*L), 1.0/(mcSteps*mcSteps*L*L)
tm = 2.269;    T=np.random.normal(tm, .64, nt)
T  = T[(T>1.2) & (T<3.8)];    nt = np.size(T)

Energia       = np.zeros(nt);   Magnetização  = np.zeros(nt)
Calorespecifico = np.zeros(nt);   Susceptibilidade = np.zeros(nt)
##############################################################################


for m in range(len(T)):
    E1 = M1 = E2 = M2 = 0
    config = initialstate(L)
    iT=1.0/T[m]; iT2=iT*iT;
    
    for i in range(eqSteps):         # Equilibrio
        mcmove(config, iT)           # Passos Monte Carlo 

    for i in range(mcSteps):
        mcmove(config, iT)           
        Ene = calcEnergy(config)     # calculo da energia com base na configuração
        Mag = calcMag(config)        # calculo da magnetização com base na configuração

        E1 = E1 + Ene
        M1 = M1 + Mag
        M2 = M2 + Mag*Mag 
        E2 = E2 + Ene*Ene

        Energia[m]         = n1*E1
        Magnetização[m]  = n1*M1
        Calorespecifico[m]   = (n1*E2 - n2*E1*E1)*iT2 # [{E²}-{E}²]/T² E=energia
        Susceptibilidade[m] = (n1*M2 - n2*M1*M1)*iT # [{M²}-{M}²]/T² M=Magnetização