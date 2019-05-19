
headerXML = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <part-list>
    <score-part id= "P1">
      <part-name> Piano </part-name>
      <score-instrument id="P1-I1">
        <instrument-name>Piano</instrument-name>
        </score-instrument>
      </score-part>
    </part-list>
  <part id="P1">
    '''

class MakeXml():

    div = 1
    def __init__(self, part):

        self.partId = "P1"
        if part != None:
            if part.compassos != None:
                self.compassos = part.compassos
            if part.partID != None:
                self.partId = part.partID
            if part.partName != None:
                self.partName = part.partName

    def montaCompasso(compasso, numCompasso, xmlFile):
        texto = '''<measure number="'''+str(numCompasso)+'''">
      '''

        if compasso.temAtributos == True:
            MakeXml.div = int(compasso.divisoes, 10)
            print(MakeXml.div)
            texto = texto + '''<attributes>
        <divisions>'''+compasso.divisoes+'''</divisions>
        <key>
          <fifths>'''+compasso.tomCicloQuintas+'''</fifths>
          </key>
        <time>
          <beats>'''+compasso.batidas+'''</beats>
          <beat-type>'''+compasso.tipoBatida+'''</beat-type>
          </time>
        <clef>
          <sign>'''+compasso.sinalClave+'''</sign>
          <line>'''+compasso.linhaClave+'''</line>
          </clef>
        </attributes>
     '''

        for nota in compasso.notas:
            if nota.tipoNota == "3":
                nota.duracao = MakeXml.div / 4
            if nota.tipoNota == "4":
                nota.duracao = MakeXml.div / 2
            if nota.tipoNota == "5":
                nota.duracao = MakeXml.div #>>>>semínima
            if nota.tipoNota == "6":
                nota.duracao = 2*MakeXml.div
            if nota.tipoNota == "7":
                nota.duracao = 4*MakeXml.div

            texto = texto + ''' <note>
        <pitch>
            <step>'''+nota.degrau+'''</step>
            <octave>'''+nota.oitava+'''</octave>
            </pitch>
        <duration>'''+str(nota.duracao)+'''</duration>
        <type>'''+nota.tipoIngles+'''</type>
        </note>
     '''
        texto = texto + '''</measure>
  '''
        xmlFile.write(texto)

    def _montaXML(self):

        xmlFile = open('/home/jose/Desktop/partituraGerada.xml', 'w')
        xmlFile.write(headerXML)
        cont = 1
        for compasso in self.compassos:
            MakeXml.montaCompasso(compasso, cont, xmlFile)
            cont += 1

        texto ='''</part>
</score-partwise>'''
        xmlFile.write(texto)

def main():

    import nota, compasso, partitura, os
    n1 = nota.Nota("G4", "5")
    n2 = nota.Nota("C4", "4")
    n3 = nota.Nota("D4", "4")
    n4 = nota.Nota("E4", "4")
    n5 = nota.Nota("F4", "4")
    n6 = nota.Nota("G4", "5")
    n7 = nota.Nota("C4", "5")
    n8 = nota.Nota("C4", "5")

    #divisoes, tomCicloQuintas, batida, tipoBatida, clave
    a = ["2", "0", "3", "4", "G"]

    notas1 = [n1, n2, n3,n4, n5]
    notas2 = [n6, n7, n8]

    comp1 = compasso.Compasso(notas1, a)
    comp2 = compasso.Compasso(notas2)

    part = partitura.Partitura([comp1, comp2])

    montador = MakeXml(part)
    montador._montaXML()
    os.system('mscore /home/jose/Desktop/partituraGerada.xml')

main()
