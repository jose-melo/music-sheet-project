

class Acorde():

    def __init__(self, notas=None, name="C"):

        if notas != None:
            self.notas = notas

        self.ehAcorde = True

        self.name = name
