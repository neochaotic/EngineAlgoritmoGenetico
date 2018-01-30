import csv, datetime,unittest, genetico

#fitness
def avalia_aptidao(genes, regras, indiceEstadoLookup):
    regraAprovada = sum(1 for regra in regras
                        if regra.EValido(genes, indiceEstadoLookup))
    return regraAprovada


def carrega_dados(nomearquivo):
    with open(nomearquivo, mode='r') as dentroArquivo:
        leitor = csv.reader(dentroArquivo)
        lookup = {linha[0]: linha[1].split(';') for linha in leitor if linha}
    return lookup


class ColorindoGrafostests(unittest.TestCase):

    def test(self):
        estados = carrega_dados("adjacent_states.csv")
        regras = contruir_regras(estados)
        valorOtimo = len(regras)
        indiceEstadoLookup = {key: index
                              for index, key in enumerate(sorted(estados))}

        cores = ["laranja", "Amarelo", "Verde", "Azul"]
        corLookup = {cor[0]: cor for cor in cores}
        geneset =  list(corLookup.keys())

        iniciaTempo = datetime.datetime.now()

        def fnTela(candidato):
            tela(candidato, iniciaTempo)

        def fnAptidao(genes):
            return avalia_aptidao(genes, regras, indiceEstadoLookup)


        melhor =  genetico.oMelhor(fnAptidao, len(estados),
                                   valorOtimo, geneset, fnTela )
        self.assertTrue(not valorOtimo > melhor.Aptidao)
        chaves = sorted(estados.keys())
        for indice  in range (len(estados)):
            print (chaves[indice] + "é" +corLookup[melhor.Genes[indice]])

def tela(candidato, inciaTempo):
    timeDiff = datetime.datetime.now() - inciaTempo
    print("{}\t{}\t{}".format(
        ''.join(map(str, candidato.Genes)),
        candidato.Aptidao, timeDiff))



class Regra:

    def __init__(self, no, adjacente):
        if no < adjacente:
            no, adjacente = adjacente, no
        self.No = no
        self.Adjacente = adjacente

    def __eq__(self, other):
        return self.No == other.No and self.Adjacente == other.Adjacente

    def __hash__(self):
        return hash(self.No) *397 ^ hash(self.Adjacente)

    def __str__(self):
        return self.No + " -> " + self.Adjacente

    def EValido(self, genes, noIndiceLookup):
        indice = noIndiceLookup[self.No]
        adjIndice = noIndiceLookup[self.Adjacente]
        return genes[indice] != genes[adjIndice]


def contruir_regras(items):
    regrasAdd =  {}

    for estado, adjacente in items.items():
        for estadoadjacente in adjacente:
            if estadoadjacente == '':
                continue
            regra =  Regra(estado, estadoadjacente)
            if regra in regrasAdd:
                regrasAdd[regra] += 1
            else:
                regrasAdd[regra] = 1

    for k, v in regrasAdd.items():
        if v != 2:
            print("Regra {} não é bidirecional".format(k))
    return regrasAdd.keys()






