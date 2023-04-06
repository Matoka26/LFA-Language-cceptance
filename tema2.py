with open("input1.txt" , 'r')as f:
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
                    dicLitereExp[caracter] = {}
    #valorile dictionarului sunt dictionare  care au ca cheie constrangerea si valoare numarul de care sunt legate
    for litera in dicLitereExp:
         constraints = f.readline().strip().split()
         for cons in constraints:
             if cons[0] == '!':
                 dicLitereExp[litera]['!'] = cons[1:].split(',')
             if cons[1] == '-':
                 dicLitereExp[litera]['>'] = '-1'
             elif cons[0] == '>':
                 dicLitereExp[litera]['>'] = cons[1:]
             if cons[0] == '<':
                 dicLitereExp[litera]['<'] = cons[1:]
         #daca nu se specifica nr minim de aparitii al literei pe pozitie o sa fie considerat 0
         if '>' not in dicLitereExp[litera].keys():
             dicLitereExp[litera]['>'] = '0'
            
            

    print(listaLitere)
    print(listaExponenti)
for litera in dicLitereExp:
    print(litera,"->",dicLitereExp[litera])

##daca nu mi dai bounds pt o litera m-ai spart
