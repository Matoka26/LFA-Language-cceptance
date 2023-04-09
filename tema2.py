
def ecuatia(ec,rez):
    ind = 0
    for i in range(len(ec)-1,0,-1):
        if ord(ec[i]) >= 97 and ord(ec[i]) <= 122:
            ind = i
            break
    if ind != len(ec)-1:
        rez = rez - int(ec[ind+1:])
    if ind != 0:
        rez = rez / int(ec[:ind-1])
    return rez

def getLitera(ec):
    for caracter in ec:
        if ord(caracter) >= 97 and ord(caracter) <= 122:
            return caracter

queue = []

with open("gramatica2.txt", 'r')as f:
    listaLitere = list(f.readline().strip()) #face o lista de litere
    listaExponenti = f.readline().strip().split() #fiecare exponent coincide ca index cu litera peste care e
    dicLitereExp = {}
    #creaza dictionaru cu literele care apar la exponent
    #daca e doar o cifra o lasa asa,nu i mai face dic
    for i in range(len(listaExponenti)):
        if listaExponenti[i].isdigit():
            listaExponenti[i] = listaExponenti[i]
        else:
            elemente = list(listaExponenti[i])
            for caracter in elemente:
                if ord(caracter) >= 97 and ord(caracter) <= 122 and caracter not in dicLitereExp.keys():
                    dicLitereExp[caracter] = {'>':-1} #toate aparitiile de litere trebuie sa fie >-1

    constraints = f.read().split("\n") #ai grija sa nu ai un \n de care nu stii
    for cons in constraints:
        if cons[1] == '>':
            dicLitereExp[cons[0]]['>'] = int(cons[2:])
        if cons[1] == '=':
            dicLitereExp[cons[0]]['='] = cons[2:]     #asta va fi folosit doar cu un OR/AND valoarea este si in < sau >

#citim din alt fisier cuvintele pe care sa le testam
with open("input1.txt" , 'r')as g:
    listaCuvinte = g.read().split('\n')     #ai grija la \n ala

# print(listaLitere)
# print(listaExponenti)
# for litera in dicLitereExp:
#     print(litera,"->",dicLitereExp[litera])
# print()
#print(listaCuvinte)
cuvinteOk = {}
for cuvant in listaCuvinte:
    hatz = 0
    dicSolutii = {}  # aici bagam ce valori gasim pentru literele de la exponenti
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
            cateLitere = "neacceptat"        #daca o litera nu e in modelul dat papa
            queue.append(f'{cuvant}-->neacceptat')
    # verificam daca aparitiile literelor sunt de forma exponentilor si vedem cat e litera
    if cateLitere != 'neacceptat':
        for i in range(len(cateLitere)):
            if listaExponenti[i].isdigit():
                if int(listaExponenti[i]) != cateLitere[i]:
                    break
            elif len(listaExponenti[i]) == 1:
                dicSolutii[getLitera(listaExponenti[i])] = cateLitere[i]
            elif len(listaExponenti[i]) > 1:
                dicSolutii[getLitera(listaExponenti[i])] = ecuatia(listaExponenti[i],cateLitere[i])
                # daca rezultatu ecuatiei e float nu e bn
                if dicSolutii[getLitera(listaExponenti[i])] != int(dicSolutii[getLitera(listaExponenti[i])]):
                    queue.append(f'{cuvant}-->neacceptat')
                    hatz = 1
                    break
        #verificam pt fiecare litera din exponent daca indeplineste conditiile de existenta
        if hatz != 1:
            for literaKey in dicLitereExp.keys():
                if literaKey not in dicSolutii.keys() and hatz != 1:
                    queue.append(f'{cuvant}-->neacceptat')
                    hatz = 1
        if hatz == 0:
            cuvinteOk[cuvant] = dicSolutii


for cuvant in cuvinteOk:
    oke = 1
    for litera in cuvinteOk[cuvant]:
        if cuvinteOk[cuvant][litera] > dicLitereExp[litera]['>']:
            if '=' in dicLitereExp[litera]:
                if cuvinteOk[cuvant][litera] != cuvinteOk[cuvant][dicLitereExp[litera]['=']]:
                    oke = 0
        else:
            oke = 0
    if oke == 1:
        print(f'{cuvant}-->acceptat')
    else:
        queue.append(f'{cuvant}-->neacceptat')
for propozitie in queue:
    print(propozitie)

