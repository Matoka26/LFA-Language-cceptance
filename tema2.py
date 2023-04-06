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
        if cons[2] == '-':
            dicLitereExp[cons[0]]['>'] = '-1'
        elif cons[1] == '>':
            dicLitereExp[cons[0]]['>'] = cons[3:]
        if cons[1] == '<':
            dicLitereExp[cons[0]]['<'] = cons[2:]

with open("input1.txt" , 'r')as g:
    listaCuvinte = g.read().split('\n')     #ai grija la \n ala

print(listaLitere)
print(listaExponenti)
for litera in dicLitereExp:
    print(litera,"->",dicLitereExp[litera])
