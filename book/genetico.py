import random


def _mutacao(pais):
    indice = random.randrange(0, len(pais)) #funçao random.range(start,stop,step)
    geneFilho = list(pais) #tranforma em lista
    novoGene, alternar = random.sample(geneSet, 2) #atribuição multipla de variaveis
    geneFilho[indice] = alternar \
        if novoGene == geneFilho[indice] \
            else novoGene
    return ''.join(geneFilho)

def _gerar_pais(tamanho):
    genes = []
    while len(genes) < tamanho:
        tamanhoAmostra = min(tamanho - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, tamanhoAmostra))
    return ''.join(genes)