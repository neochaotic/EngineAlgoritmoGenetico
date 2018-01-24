import random
import statistics
import time
import sys


def _mutacao(pais, geneSet,avalia_aptidao):
    indice = random.randrange(0, len(pais.Genes)) #funçao random.range(start,stop,step)
    geneFilho = pais.Genes[:]
    novoGene, alternar = random.sample(geneSet, 2) #atribuição multipla de variaveis
    geneFilho[indice] = alternar \
        if novoGene == geneFilho[indice] \
            else novoGene
    aptidao = avalia_aptidao(geneFilho)
    return Cromossomo(geneFilho, aptidao)

def _gerar_pais(tamanho, geneSet, avalia_aptidao):
    genes = []
    while len(genes) < tamanho:
        tamanhoAmostra = min(tamanho - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, tamanhoAmostra))
    aptidao = avalia_aptidao(genes)
    return Cromossomo(genes, aptidao)


def oMelhor(avalia_aptidao, tamanhoAlvo, aptidaoOtima, geneSet, tela ):
    random.seed()
    #inicioTempo = datetime.datetime.now()
    melhorPai = _gerar_pais(tamanhoAlvo, geneSet, avalia_aptidao)
    #melhorAptidao = avalia_aptidao(melhorPai)
    tela(melhorPai)
    if melhorPai.Aptidao >= aptidaoOtima:
        return melhorPai

    while True:
        filho = _mutacao(melhorPai, geneSet, avalia_aptidao)

        #aptidaoFilho = avalia_aptidao(filho)

        if melhorPai.Aptidao >= filho.Aptidao:
            continue
        tela(filho)
        if filho.Aptidao >= aptidaoOtima:
            return filho
        melhorPai = filho

class Cromossomo:
    def __init__(self, genes, aptidao,):
        self.Genes = genes
        self.Aptidao = aptidao



class Benchmark:
    @staticmethod
    def run(funcao):

        cronometragem = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            iniciaTempo = time.time()
            funcao()
            segundos = time.time() - iniciaTempo
            sys.stdout = stdout
            cronometragem.append(segundos)
            media = statistics.mean(cronometragem)
            if i < 10 or  i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(
                    1 + i, media,
                    statistics.stdev(cronometragem,media)
                    if i > 1 else 0))
