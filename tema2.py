with open("gramatica1.txt", 'r')as f:
    listaLitere = list(f.readline().strip()) #face o lista de litere
    listaExponenti = f.readline().strip().split() #fiecare exponent coincide ca index cu litera peste care e
    dicLitereExp = {}
    #creaza dictionaru cu literele care apar la exponent
    #daca e doar o cifra o lasa asa,nu i mai face dic
    for i in range(len(listaExponenti)):
        if listaExponenti[i].isdigit():
            listaExponenti[i] = int(listaExponenti[i])
        else:
            elemente = list(listaExponenti[i])
            for caracter in elemente:
                if ord(caracter) >= 97 and ord(caracter) <= 122 and caracter not in dicLitereExp.keys():
                    dicLitereExp[caracter] = {'>':'-1'} #toate aparitiile de litere trebuie sa fie >-1

    constraints = f.read().split("\n") #ai grija sa nu ai un \n de care nu stii
    for cons in constraints:
        if cons[1] == '!':
            dicLitereExp[cons[0]]['!'] = list(cons[2:].split(','))
        if cons[1] == '>':
            dicLitereExp[cons[0]]['>'] = cons[2:]
        if cons[1] == '<':
            dicLitereExp[cons[0]]['<'] = cons[2:]
        if cons[1] == '=':
            dicLitereExp[cons[0]]['='] = cons[2:]      #asta va fi folosit doar cu un OR/AND valoarea este si in < sau >

#citim din alt fisier cuvintele pe care sa le testam
with open("input1.txt" , 'r')as g:
    listaCuvinte = g.read().split('\n')     #ai grija la \n ala

print(listaLitere)
print(listaExponenti)
for litera in dicLitereExp:
    print(litera,"->",dicLitereExp[litera])

#print(listaCuvinte)

for cuvant in listaCuvinte:
    cateLitere = [0] * (len(listaLitere))
    i = 0
    j = 0
    while i < len(cuvant) and j < len(listaLitere):
        if cuvant[i] == listaLitere[j]:
            cateLitere[j] += 1
            i += 1
        else:
            j += 1
        if j == len(listaLitere):
            cateLitere = "abort"        #daca o litera nu e in modelul dat papa
    print(cuvant,"--->",cateLitere)
