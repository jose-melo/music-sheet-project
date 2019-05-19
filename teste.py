
def main():

    headerXML = '''
<?xml version="1.0" encoding="UTF-8"?>
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
'''

    headerXML = headerXML +    '''XABLAAAAAU'''

    #arq = open('/home/jose/Desktop/xablau.xml', 'w')
    #arq.write(headerXML)
    #arq.close()

    print(nomeDaNota("4")[0])

def nomeDaNota(num):
    switcher = {
        "3":["semi-colcheia", "sixteenth"],
        "4":["colcheia", "eighth"],
        "5":["semínima", "quarter"],
        "6":["mínima", "half"],
        "7":["semibreve", "whole"]
    }
    return switcher.get(num, ["Nota invalida", "Invalid note"])




main()
