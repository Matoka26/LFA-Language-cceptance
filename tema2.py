with open("input1.txt" , 'r')as f:
    listaLitere = list(f.readline().strip()) #face o lista de litere
    listaExponenti = f.readline().strip().split() #fiecare exponent coincide ca index cu litera peste care e
    dicLitereExp = {}
    #creaza dictionaru cu literele care apar la exponent
    for i in range(len(listaExponenti)):
        elemente = list(listaExponenti[i])
        for caracter in elemente:
            if ord(caracter) >= 97 and ord(caracter) <= 122 and caracter not in dicLitereExp.keys():
                dicLitereExp[caracter] = {}
    #valorile dictionarului sunt dictionare  care au ca cheie constrangerea si valoare numarul de care sunt legate
    for litera in dicLitereExp:
         constraints = f.readline().strip().split()
         for cons in constraints:
             if cons[0] == '!':
                 dicLitereExp[litera]['!'] = [int(x) for x in cons[1:].split(',')]
             if cons[1] == '-':
                 dicLitereExp[litera]['>'] = 0
             elif cons[0] == '>':
                 dicLitereExp[litera]['>'] = int(cons[1:])
             if cons[0] == '<':
                 dicLitereExp[litera]['<'] = int(cons[1:])



    print(listaLitere)
    print(listaExponenti)
for litera in dicLitereExp:
    print(litera,"->",dicLitereExp[litera])