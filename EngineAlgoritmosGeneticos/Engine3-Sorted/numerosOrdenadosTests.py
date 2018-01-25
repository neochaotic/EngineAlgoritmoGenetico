import unittest
import datetime
import genetico


class Aptidao:
    def __init__(self, contaSequencia, totalGap):
        self.ContaSequencia = contaSequencia
        self.TotalGap = totalGap

    def __gt__(self, other):
        if self.ContaSequencia != other.ContaSequencia:
            return self.ContaSequencia > other.ContaSequencia
        return self.TotalGap < other.ContaSequencia

    def __str__(self):
        return "{} Sequencial, {} Gap Total,".format(
            self.ContaSequencia, self.TotalGap)


class NumerosOrdenadosTests(unittest.TestCase):

    def test_ordena_10_numeros(self):
        self.ordena_numeros(10)

    def ordena_numeros(self, totalNumeros):
        geneSet = [i for i in range(100)]
        iniciaTempo = datetime.datetime.now()

        def fnTela(candidato):
            tela(candidato, iniciaTempo)

        def fnAptidao(genes):
            return avalia_apitidao(genes)

        aptidaoOtima = Aptidao(totalNumeros, 0)
        melhor = genetico.oMelhor(fnAptidao, totalNumeros,
                                  aptidaoOtima, geneSet, fnTela)
        self.assertTrue(not aptidaoOtima > melhor.Aptidao)
    """ olhar esse teste trava tudo
    def test_benchmark(self):
        genetico.Benchmark.run(lambda: self.ordena_numeros(40))
    """

def avalia_apitidao(genes):
    aptidao = 1
    gap = 0
    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            aptidao += 1
        else:
            gap += genes[i - 1] - genes[i]
    return Aptidao(aptidao, gap)


def tela(candidato, iniciaTempo):
    timeDiff = datetime.datetime.now() - iniciaTempo
    print("{}\t=> {}\t{}".format(
        ', '.join(map(str, candidato.Genes)),
        candidato.Aptidao,
        timeDiff))


if __name__ == '__main__':
    unittest.main()
