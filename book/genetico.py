import random


def _mutacao(pais, geneSet):
    indice = random.randrange(0, len(pais)) #funçao random.range(start,stop,step)
    geneFilho = list(pais) #tranforma em lista
    novoGene, alternar = random.sample(geneSet, 2) #atribuição multipla de variaveis
    geneFilho[indice] = alternar \
        if novoGene == geneFilho[indice] \
            else novoGene
    return ''.join(geneFilho)

def _gerar_pais(tamanho, geneSet):
    genes = []
    while len(genes) < tamanho:
        tamanhoAmostra = min(tamanho - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, tamanhoAmostra))
    return ''.join(genes)

def oMelhor(avalia_aptidao, tamanhoAlvo, aptidaoOtima, geneSet, tela ):
    random.seed()
    #inicioTempo = datetime.datetime.now()
    melhorPai = _gerar_pais(tamanhoAlvo, geneSet)
    melhorAptidao = avalia_aptidao(melhorPai)
    tela(melhorPai)
    if melhorAptidao >= aptidaoOtima:
        return melhorPai

    while True:
        filho = _mutacao(melhorPai, geneSet)
        aptidaoFilho = avalia_aptidao(filho)

        if melhorAptidao >= aptidaoFilho:
            continue
        tela(filho)
        if aptidaoFilho >= aptidaoOtima:
            return filho
        melhorAptidao = aptidaoFilho
        melhorPai = filho