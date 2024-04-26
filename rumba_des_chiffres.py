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

def estBut(e,but) :
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

def profondeurMalPlace(e,but):
    res = 0
    for i in range(len(e)):
        e_p = [0] * (len(but[i]) - len(e[i])) + e[i]
        but_p = [0] * (len(e[i]) - len(but[i])) + but[i]
        for j in range(len(e_p)):
            if e_p[j] != but_p[j] and e_p[j] != 0 :
                res += j
    return res

def ProfondeurBornee(etat,but,g,seuil,chemin) :
    f = g + profondeurMalPlace(etat,but)

    if f > seuil :
        return f
    
    if estBut(etat,but) :
        chemin.append(etat)
        return True
    
    nSeuil = float('inf')
    chemin.append(etat)
    for e in opPos(etat) :
        if e[1] not in chemin :
            trouve = ProfondeurBornee(e[1],but,g+1,seuil,chemin)
            if trouve == True : 
                if len(chemin) == 1 : chemin.append(e[1])
                return True
            if trouve < nSeuil : nSeuil = trouve
    chemin.remove(etat)
    
    return nSeuil

def IDAStar(init,but) :
    seuil = profondeurMalPlace(init,but)
    chemin = []

    while True :
        trouve = ProfondeurBornee(init,but,0,seuil,chemin)
        if trouve == True : return chemin
        elif trouve == float('inf') : return []
        else : seuil = trouve

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

res = IDAStar(RumbaGame,but)
if res :
    for e in res :
        afficherEtat(e)
    print(len(res))
else : 
    print("Echec de la resolution" )