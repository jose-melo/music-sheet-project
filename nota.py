
class Nota():

    def __init__(self, alturaNota=None, tipoNota="5"):

        self.degrau = ""
        self.tipoIngles = ""
        self.acidente = ""
        self.oitava = ""
        self.nomeCompleto = ""
        self.duracao = 1

        if alturaNota != None and len(alturaNota) == 3 or len(alturaNota) == 2:

            if alturaNota[0] >= 'A' and alturaNota[0] <= 'G':
                self.degrau = alturaNota[0]

            if alturaNota[1] == 'b' or alturaNota[1] == '#':
                self.acidente = alturaNota[1]

                if alturaNota[2] >= '1' and alturaNota[2] <= '9':
                    self.oitava = alturaNota[2]

            elif alturaNota[1] >= '1' and alturaNota[1] <= '9':
                self.oitava = alturaNota[1]

        if tipoNota != None:
            self.tipoNota = tipoNota

        self.tipoIngles = self.nomeDaNota()[1]
        self.nomeCompleto = self.degrau + self.oitava

    def __repr__(self):
        return '<nota.Nota %s ' % self.nomeCompleto + ' %s ' % self.nomeDaNota()[0]


    def nomeDaNota(self):
        switcher = {
            "3":["semi-colcheia", "sixteenth"],
            "4":["colcheia", "eighth"],
            "5":["seminima", "quarter"],
            "6":["minima", "half"],
            "7":["semibreve", "whole"]
        }
        return switcher.get(self.tipoNota, ["Nota invalida", "Invalid note"])


#lixo = Nota("C4")
#print(lixo.nomeDaNota())
