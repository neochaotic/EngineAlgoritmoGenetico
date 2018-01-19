
import random

import datetime



def gerar_pais(tamanho):
    genes = []
    while len(genes) < tamanho:
        tamanhoAmostra = min(tamanho - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, tamanhoAmostra))
    return ''.join(genes)

def avalia_aptidao(adivinha):
    return sum(1 for esperado, atual in zip(alvo, adivinha) #bem confusa essa iteração ver mais
                if esperado == atual)


def mutacao(pais):
    indice = random.randrange(0, len(pais)) #funçao random.range(start,stop,step)
    geneFilho = list(pais) #tranforma em lista
    novoGene, alternar = random.sample(geneSet, 2) #atribuição multipla de variaveis
    geneFilho[indice] = alternar \
        if novoGene == geneFilho[indice] \
            else novoGene
    return ''.join(geneFilho)


def tela(adivinha):
    timeDiff = datetime.datetime.now() #-startTime
    aptidao = avalia_aptidao(adivinha)
    print ("{}\t{}\t{}".format(adivinha, aptidao, timeDiff))

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.1234567890"
alvo = "Python eh 42!"



random.seed()
inicioTempo = datetime.datetime.now()
melhorPai = gerar_pais(len(alvo))
melhorAptidao = avalia_aptidao(melhorPai)
tela(melhorPai)

while True:
    filho = mutacao(melhorPai)
    aptidaoFilho = avalia_aptidao(filho)
    if melhorAptidao >= aptidaoFilho:
        continue
    tela(filho)
    if aptidaoFilho >= len(melhorPai):
        break
    melhorAptidao = aptidaoFilho
    melhorPai = filho






