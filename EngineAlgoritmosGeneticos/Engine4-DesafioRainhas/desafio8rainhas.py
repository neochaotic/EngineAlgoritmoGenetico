import unittest
import datetime
import genetico


class Aptidao:
    def __init__(self, total):
        self.Total = total

    def __gt__(self, other):
        return self.Total < other.Total

    def __str__(self):
        return "{}".format(self.Total)

def avalia_aptidao(genes, tamanho):
    tabuleiro = Tabuleiro(genes, tamanho)
    linhasComRainhas = set()
    colunasComRainhas = set()
    nortOesteDiagonalComRainhas = set()
    sulOesteDiagonalcomRainhas = set()
    for linha in  range(tamanho):
        for col in range(tamanho):
            if tabuleiro.get(linha,col) == 'Q':
                linhasComRainhas.add(linha)
                colunasComRainhas.add(col)
                nortOesteDiagonalComRainhas.add(linha + col)
                sulOesteDiagonalcomRainhas.add(tamanho -1 - linha + col)

    total =  tamanho - len(linhasComRainhas) \
             + tamanho - len(colunasComRainhas) \
             + tamanho - len(nortOesteDiagonalComRainhas) \
             + tamanho - len(sulOesteDiagonalcomRainhas)

    return Aptidao(total)


class OitoRainhasTests(unittest.TestCase):

    def test(self, tamanho=8):
        geneset = [i for i in range(tamanho)]
        iniciaTempo = datetime.datetime.now()

        def fnTela(candidato):
            tela(candidato, iniciaTempo, tamanho)

        def fnAptidao(genes):
            return avalia_aptidao(genes, tamanho)

        aptidaoOtima = Aptidao(0)
        melhor = genetico.oMelhor(fnAptidao, 2 * tamanho,
                                  aptidaoOtima, geneset, fnTela)
        self.assertTrue(not aptidaoOtima > melhor.Aptidao)

    def test_benchmark(self):
        genetico.Benchmark.run(lambda: self.test(20))

class Tabuleiro:

    def __init__(self, genes, tamanho):
        tabuleiro = [['.']*tamanho for _ in range(tamanho)]
        for indice in range(0, len(genes), 2):
            linha = genes[indice]
            coluna = genes[indice + 1]
            tabuleiro[coluna][linha] = 'Q'
        self._tabuleiro = tabuleiro

    def get(self, linha, col):
        return self._tabuleiro[col][linha]


    def print(self):
        for i in reversed(range(0, len(self._tabuleiro))):
            print(' '.join(self._tabuleiro[i]))

def tela(candidato, iniciaTempo, tamanho):
    timeDiff = datetime.datetime.now() - iniciaTempo
    tabuleiro = Tabuleiro(candidato.Genes, tamanho)
    tabuleiro.print()
    print("{}\t- {}\t{}".format(
        ' '.join(map(str, candidato.Genes)),
        candidato.Aptidao, timeDiff))

if __name__ == '__main__':
    unittest.main()