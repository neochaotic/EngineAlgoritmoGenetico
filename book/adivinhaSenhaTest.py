import datetime
import genetico

import unittest


class adivinhaSenhaTeste(unittest.TestCase):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Hello_World(self):
        alvo = "Hello World"
        self.adivinha_senha(alvo)

    def test_longo(self):
        alvo = "O rato roeu a roupa do rei de Roma!!!"
        self.adivinha_senha(alvo)

    def adivinha_senha(self, alvo):

        iniciaTempo = datetime.datetime.now()

        def fnAptidao(genes):
            return avalia_aptidao(genes, alvo)

        def fnTela(genes):
            tela(genes, alvo, iniciaTempo  )

        aptidaoOtima = len(alvo)
        melhor = genetico.oMelhor(fnAptidao, len(alvo),
                    aptidaoOtima, self.geneSet, fnTela)

def tela(genes, alvo, iniciaTempo):
    timeDiff = datetime.datetime.now() #- startTime
    aptidao = avalia_aptidao(genes, alvo)
    print("{}\t{}\t{}".format(genes, aptidao, timeDiff))

def avalia_aptidao(genes, alvo):
    return sum(1 for esperado, atual in zip(alvo, genes)
               if esperado == atual)


if __name__ == '__main__':
    unittest.main()

