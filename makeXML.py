
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


    def pegaDuracao (nota):
        retorno = 0
        if nota.tipoNota == "3":
            retorno = MakeXml.div / 4
        if nota.tipoNota == "4":
            retorno = MakeXml.div / 2
        if nota.tipoNota == "5":
            retorno = MakeXml.div #>>>>semínima
        if nota.tipoNota == "6":
            retorno = 2*MakeXml.div
        if nota.tipoNota == "7":
            retorno = 4*MakeXml.div
        return retorno

    def montaNotas(nota):
        nota.duracao = MakeXml.pegaDuracao(nota)
        texto = ''' <note>
        <pitch>
            <step>'''+nota.degrau+'''</step>
            <octave>'''+nota.oitava+'''</octave>
            </pitch>
        <duration>'''+str(nota.duracao)+'''</duration>
        <type>'''+nota.tipoIngles+'''</type>
        </note>
     '''
        return texto

    def montaAcorde(acorde):
        cont = 1
        val = ''''''
        texto = ""
        for nota in acorde.notas:
            nota.duracao = MakeXml.pegaDuracao(nota)
            if cont != 1 :
                texto = texto + '''<note>
        <chord/>
        <pitch>
          <step>'''+nota.degrau+'''</step>
          <octave>'''+nota.oitava+'''</octave>
          </pitch>
        <duration>'''+str(nota.duracao)+'''</duration>
        <type>'''+nota.tipoIngles+'''</type>
        </note>
    '''
            else:
                texto = texto + '''<note>
        <pitch>
          <step>'''+nota.degrau+'''</step>
          <octave>'''+nota.oitava+'''</octave>
          </pitch>
        <duration>'''+str(nota.duracao)+'''</duration>
        <type>'''+nota.tipoIngles+'''</type>
        </note>
     '''
            cont += 1
        return texto

    def montaCompasso(compasso, numCompasso, xmlFile):
        texto = '''<measure number="'''+str(numCompasso)+'''">
      '''

        if compasso.temAtributos == True:
            MakeXml.div = int(compasso.divisoes, 10)
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

            if nota.ehAcorde == True:
                texto = texto + '''<harmony print-frame="no">
       <root>
         <root-step>'''+nota.name+'''</root-step>
         </root>
         <kind text="C">major</kind>
    </harmony>
    '''
                texto = texto + MakeXml.montaAcorde(nota)
            else:
                texto = texto + MakeXml.montaNotas(nota)

        texto = texto + '''</measure>
  '''
        xmlFile.write(texto)

    def _montaXML(self):

        xmlFile = open('/home/jose/Desktop/AutomatizaPartitura/partituraGerada.xml', 'w')
        xmlFile.write(headerXML)
        cont = 1
        for compasso in self.compassos:
            MakeXml.montaCompasso(compasso, cont, xmlFile)
            cont += 1

        texto ='''</part>
</score-partwise>'''
        xmlFile.write(texto)

def main():

    import nota, compasso, partitura, os, acorde
    n1 = nota.Nota("C4", "5")
    n2 = nota.Nota("E4", "5")
    n3 = nota.Nota("G4", "5")

    #divisoes, tomCicloQuintas, batida, tipoBatida, clave
    a = ["1", "0", "4", "4", "G"]

    notas1 = [n1, n2, n3]
    acord1 = acorde.Acorde(notas1, "C")
    acord2 = acorde.Acorde(notas1, "D")
    acord3 = acorde.Acorde(notas1, "E")

    comp1 = compasso.Compasso([n1, n2, n3], a)

    part = partitura.Partitura([comp1])

    montador = MakeXml(part)
    montador._montaXML()
    os.system('mscore /home/jose/Desktop/AutomatizaPartitura/partituraGerada.xml')

main()
