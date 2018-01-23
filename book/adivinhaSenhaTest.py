import datetime
import genetico
import unittest
import random

class adivinhaSenhaTeste(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Hello_World(self):
        alvo = "Hello World"
        self.adivinha_senha(alvo)

    def test_benchmark(self):
        genetico.Benchmark.run(self.test_longo)

    def test_longo(self):
        alvo = "O rato roeu a roupa do rei de Roma!!!"
        self.adivinha_senha(alvo)

    def test_Randomico(self):
        tamanho = 150
        alvo = ''.join(random.choice(self.geneset) for _ in range(tamanho))
        self.adivinha_senha(alvo)

    def test_benchmar(self):
        genetico.Benchmark.run(self.test_Randomico)

    def adivinha_senha(self, alvo):

        iniciaTempo = datetime.datetime.now()

        def fnAptidao(genes):
            return avalia_aptidao(genes, alvo)

        def fnTela(candidato):
            tela(candidato, iniciaTempo)

        aptidaoOtima = len(alvo)
        melhor = genetico.oMelhor(fnAptidao, len(alvo),
                        aptidaoOtima, self.geneset, fnTela)

        self.assertEqual(melhor.Genes, alvo)



def tela(candidato, iniciaTempo):
    timeDiff = datetime.datetime.now() - iniciaTempo
    print("{}\t{}\t{}".format(
        candidato.Genes, candidato.Aptidao, timeDiff))

def avalia_aptidao(adivinha, alvo):
    return sum(1 for esperado, atual in zip(alvo, adivinha)
               if esperado == atual)


if __name__ == '__main__':
    unittest.main()

