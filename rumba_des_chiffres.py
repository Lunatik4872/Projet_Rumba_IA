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

def nombreMalMis(e, but):
    res = 0
    for i in range(len(e)):
        e_padded = [0] * (len(but[i]) - len(e[i])) + e[i]
        but_padded = [0] * (len(e[i]) - len(but[i])) + but[i]
        print(e_padded,but_padded)
        for j in range(len(e_padded)):
            if e_padded[j] != but_padded[j] and e_padded[j] != 0 :
                res += 1
    return res

def heuristique(g,h) :
    return g+h

RumbaGame = [[2,3],[7,1],[4,5,6],[8,9]]
but = [[3],[2,1],[4,5,6],[7,8,9]]

# afficherEtat(RumbaGame)
# afficherEtat(but)
# print(trouverDestinations(RumbaGame,1))
# print(deplacer(RumbaGame,0,1))
# print(estBut(RumbaGame,but))
# print(opPos(RumbaGame))
# print(nombreMalMis(RumbaGame,but))
# print(heuristique(2,nombreMalMis(RumbaGame,but)))






