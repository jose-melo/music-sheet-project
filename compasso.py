

class Compasso():

    def __init__ (self, notas=None, atributos=None, id=1):
        self.id = id
        if notas != None:
            self.notas = notas

        self.divisoes = ""
        self.tomCicloQuintas = ""
        self.batidas = ""
        self.tipoBatida = ""
        self.sinalClave = ""
        self.linhaClave = ""

        self.temAtributos = False
        if atributos != None:
            self.temAtributos = True
            self.divisoes = atributos[0]
            self.tomCicloQuintas = atributos[1]
            self.batidas = atributos[2]
            self.tipoBatida = atributos[3]

            if atributos[4] == "G":
                self.sinalClave = "G"
                self.linhaClave = "2"
            elif atributos[4] == "F":
                self.sinalClave = "F"
                self.linhaClave = "4"

        self.nomeCompleto = 'Compasso %s' % id
    def __repr__(self):
        return '<Compasso.Compasso %s ' % self.nomeCompleto + ' %s ' % self.nomeDaNota()[0]

def main():
    import nota
    nota1 = nota.Nota("C4")
    nota2 = nota.Nota("D5")
    nota3 = nota.Nota("G4")

    #divisoes, tomCicloQuintas, batida, tipoBatida, clave
    a = ["1", "0", "4", "4", "G"]

    notas = [nota1, nota2, nota3]

    comp = compasso(notas, a)

    for nota in  comp.notas:
        print(nota.nomeCompleto)
