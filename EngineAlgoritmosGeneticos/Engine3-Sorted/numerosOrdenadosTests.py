import unittest
import datetime
import genetico

class NumerosOrdenadosTests(unittest.TestCase):

    def test_ordena_10_numeros(self):
        self.ordena_numeros(10)

    def ordena_numeros(self, totalNumeros):
        geneset = [i for i in range(100)]
        iniciaTempo = datetime.datetime.now()

        def fnTela(candidato):
             tela(candidato, iniciaTempo)

        def fnAptidao(genes):
            return avalia_apitidao(genes)

        aptidaoOtima = totalNumeros
        melhor = genetico.oMelhor(fnAptidao, totalNumeros,
                            aptidaoOtima, geneset, fnTela)
        self.assertTrue(not aptidaoOtima > melhor.Aptidao)


def avalia_apitidao(genes):
    aptidao = 1
    for i in range (1, len(genes)):
        if genes[i] > genes[i -1]:
            aptidao +=1
    return aptidao

def tela(candidato, iniciaTempo):
    timeDiff = datetime.datetime.now() - iniciaTempo
    print("{}\t=> {}\t{}".format(
        ', '.join(map(str, candidato.Genes)),
        candidato.Aptidao,
        timeDiff))

