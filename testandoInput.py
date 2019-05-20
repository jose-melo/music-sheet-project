def main():
    arq = open('/home/jose/Desktop/AutomatizaPartitura/input.txt', 'r')

    notes = arq.readlines()

    notes[0] = notes[0].rstrip('\n')
    a = notes[0].split(' ')
    print(a[0])

main()
