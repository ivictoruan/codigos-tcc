# https://en.wikipedia.org/wiki/Particle_swarm_optimization
from copy import deepcopy
import numpy as np

# CONSTANTES
MAX_GEN = 5
TAM_POP = 20
TAM_CROM = 2
LI = -32.768
LS = 32.768
DIMEN = 2

def GeraPopulacao(inf, sup):
    return np.random.uniform(inf, sup, size=(TAM_POP, TAM_CROM))

def Aptidao(cromossomo):
    aux = -20 * np.exp(-0.2 * np.sqrt(0.5 * (cromossomo[0] ** 2 + cromossomo[1] ** 2))) \
          - np.exp(0.5 * (np.cos(2 * np.pi * cromossomo[0]) + np.cos(2 * np.pi * cromossomo[1]))) + 20 + np.exp(1)
    return aux

pop = GeraPopulacao(LI,LS)
melhor_local = deepcopy(pop[:])
melhor_global = deepcopy(pop[0])
velocidades = np.random.uniform(-1, 1, size=(TAM_POP, TAM_CROM))


for a in range(0, TAM_POP):
    if Aptidao(melhor_local[a]) < Aptidao(melhor_global):
        melhor_global = melhor_local[a]

#ja temos inicializados: a)populacao b)melhor_local, c)melhor_global ed)velocidades

i = 1
w = 0.5
c1 = 1
c2 = 1
while(i <= MAX_GEN):
    for b in range(0, TAM_POP):
        for c in range(0, DIMEN):
            r_p = np.random.uniform(0, 1)
            r_g = np.random.uniform(0, 1)      
            vel_cog = c1 * r_p * (melhor_local[b ,c] - pop[b, c])
            vel_social = c2 * r_g * (melhor_global[c] - pop[b, c])
            velocidades[b, c] = w * velocidades[b, c] + vel_cog + vel_social
            pop[b,c] = pop[b, c] + velocidades[b, c]
            pop[b,c] = np.clip(pop[b, c], LI, LS)

        if Aptidao(pop[b]) < Aptidao(melhor_local[b]):
            melhor_local[b] = pop[b][:]
            if Aptidao(melhor_local[b]) < Aptidao(melhor_global):
                melhor_global = melhor_local[b][:]
    i = i + 1
    print(Aptidao(melhor_global))

# print("Melhor de Todas as Gerações: " + str(melhor_global) + "\t Melhor Aptidão das últimas {} Gerações: ".format(MAX_GEN) + str(Aptidao(melhor_global)))
