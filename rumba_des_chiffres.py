def afficherEtat(elt):
    maxi = max(len(sublist) for sublist in elt)
    for level in range(maxi - 1, -1, -1):
        for pipe in elt:
            if level < len(pipe) : print(pipe[-level-1], end=" ")
            else : print(" ", end=" ")
        print("")
    print("-"*len(elt)*2)

def trouverDestinations(e,pi) :
    res = []
    for i in range(len(e)) :
        if i != pi and len(e[i]) < 3 : res.append(i)
    return res

def deplacer(e,p1,p2) :
    elt = e[p1].pop(0)
    e[p2].insert(0,elt)
    return e

def estBut(e) :
    return e == but

def opPos(e):
    res = []
    for i in range(len(e)):
        if e[i]:
            possible = trouverDestinations(e, i)
            for j in possible:
                etat = [pipe[:] for pipe in e]
                etat = deplacer(etat, i, j)
                res.append(((i, j), etat, 1))
    return res

def nombreMalMis(e):
    res = 0
    for i in range(len(e)):
        e_padded = [0] * (len(but[i]) - len(e[i])) + e[i]
        but_padded = [0] * (len(e[i]) - len(but[i])) + but[i]
        for j in range(len(e_padded)):
            if e_padded[j] != but_padded[j] and e_padded[j] != 0 :
                res += 1
    return res

def heuristique(g,h) :
    return g+h

def ProfondeurBornee(seuil,etat,solution) :
    nSeuil = float('inf')
    vus = []
    enAttente = [etat]
    g = 1

    while enAttente :
        prochain = enAttente.pop()
        vus.insert(0,prochain)
        solution.append(prochain)
        if estBut(prochain) :
            return True
        else :
            g+=1
            for e in opPos(prochain) :
                h = heuristique(g,nombreMalMis(e[1]))
                if(e[1] not in vus and h <= seuil[0]) :
                    enAttente.insert(0,e[1])
                else :
                    nSeuil = min(nSeuil,h)
        
    if(nSeuil == float('inf')) : return True
    else :
        seuil[0] = nSeuil
        return False

def IDAstar(init) :
    solution = []
    seuil = [heuristique(0,nombreMalMis(init))]
    while not ProfondeurBornee(seuil,init,solution) : continue
    return solution if solution else "Echec de la resolution"

RumbaGame_1 = [[2,3],[1],[4,5,6],[7,8,9]]
RumbaGame_2 = [[1,2,3],[4,5,6],[7,8,9],[]]

but_1 = [[1,2,3],[],[4,5,6],[7,8,9]]
but_2 = [[1,2,3],[9,8,7],[4,5,6],[]]
but_3 = [[7,2,3],[8,4,6],[1,5,9],[]]
but_4 = [[2,1,3],[5,4,6],[8,7,9],[]]
but_5 = [[8,2,3],[4,6],[5,7,9],[1]]
but_6 = [[1,7,4],[2,8,5],[3,9,6],[]]

but = but_3
RumbaGame = RumbaGame_2

# afficherEtat(RumbaGame)
# afficherEtat(but)
# print(trouverDestinations(RumbaGame,1))
# deplacer(RumbaGame,0,1)
# afficherEtat(RumbaGame)
# print(estBut(RumbaGame,but))
# print(opPos(RumbaGame))
# print(nombreMalMis(RumbaGame,but))
# print(heuristique(2,nombreMalMis(RumbaGame,but)))

res = IDAstar(RumbaGame)
for e in res :
    afficherEtat(e)





