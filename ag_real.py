import numpy as np
import matplotlib.pyplot as plt

#
MAX_GEN = 50
TAM_POP = 100
TAM_CROM = 2
QT_TORNEIO = 3
TX_CROSS = 0.7
TX_MUT = 0.01
LI = -32.768
LS = 32.768

def GeraPopulacao(inf,sup):
    return np.random.uniform(inf,sup, size=(TAM_POP, TAM_CROM))

def Aptidao(cromossomo):
    aux = -20*np.exp(-0.2*np.sqrt(0.5*(cromossomo[0]**2+cromossomo[1]**2))) - np.exp(0.5*(np.cos(2*np.pi*cromossomo[0])+np.cos(2*np.pi*cromossomo[1]))) + 20+ np.exp(1)
    return 1/(1.0+aux)
    
def CalculaAptidoes(pop):
    return np.array([Aptidao(x) for x in pop])

def SelecaoTorneio(aptidoes):
    indices_cromo = np.random.randint(0,TAM_POP,size=QT_TORNEIO)
    aptidoes_selecionadas = aptidoes[indices_cromo]
    indice_melhor = np.argmax(aptidoes_selecionadas)
    return indices_cromo[indice_melhor]    
            
def Cruzamento(pai,mae):
    return ((pai+mae)/2.0)

def Mutacao(cromossomo):
    aux = cromossomo + np.random.normal(size=2)
    return np.clip(aux,LI,LS)

pop = GeraPopulacao(LI,LS)
aptidoes = CalculaAptidoes(pop)

medias = []
melhores = []

for g in range(MAX_GEN):
    
    nova_pop = []
    for c in range(TAM_POP):
        pai = pop[SelecaoTorneio(aptidoes)]
        mae = pop[SelecaoTorneio(aptidoes)]
        r = np.random.random()
        if r <= TX_CROSS:
            filho = Cruzamento(pai,mae)
        else:
            filho = pai[:]
        r = np.random.random()
        if r <= TX_MUT:
            filho = Mutacao(filho)
        r = np.random.random()            
        nova_pop.append(filho)
        
    indice_melhor_pop = np.argmax(aptidoes)
    aptidoes = CalculaAptidoes(nova_pop)
    indice_pior_nova_pop = np.argmin(aptidoes)
    nova_pop[indice_pior_nova_pop] = pop[indice_melhor_pop]
    pop = nova_pop[:]
    medias.append(np.mean(aptidoes))
    melhores.append(np.max(aptidoes))
    print ("Media: "+ str(medias[-1]) + "\t Melhor: "+str(melhores[-1]))
    

index_solucao = np.argmax(aptidoes)

print ("Resposta final: " + str(pop[index_solucao]))
