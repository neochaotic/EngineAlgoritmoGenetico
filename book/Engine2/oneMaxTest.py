import unittest
import datetime
import genetico


def avalia_aptidao(genes):
    return genes.count(1)

def tela(candidato, iniciaTempo):
    timeDiff = datetime.datetime.now() - iniciaTempo
    print("{}...{}\t{:3.2}\t{}".format(
        ''.join(map(str, candidato.Genes[:15])),
        ''.join(map(str, candidato.Genes[-15:])),
        str(candidato.Aptidao), str(timeDiff)))


class oneMaxTests(unittest.TestCase):

    def test(self, tamanho = 100):
        geneset = [0, 1]
        iniciaTempo = datetime.datetime.now()

        def fnTela(candidato):
            tela(candidato, iniciaTempo)

        def fnAptidao(genes):
            return avalia_aptidao(genes)

        aptidaoOtima = tamanho
        melhor = genetico.oMelhor(fnAptidao, tamanho, aptidaoOtima,
                                  geneset, fnTela)
        self.assertEqual(melhor.Aptidao, aptidaoOtima)

    def test_benchmark(self):
        genetico.Benchmark.run(lambda: self.test(4000))



if __name__ == '__main__':
    unittest.main()



