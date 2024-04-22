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

def profondeurMalPlace(e):
    res = 0
    for i in range(len(e)):
        e_p = [0] * (len(but[i]) - len(e[i])) + e[i]
        but_p = [0] * (len(e[i]) - len(but[i])) + but[i]
        for j in range(len(e_p)):
            if e_p[j] != but_p[j] and e_p[j] != 0 :
                res += j+1
    return res

import numpy as np

def manatthan(e) :
    res = 0
    e_np = []
    but_np = []
    for i in range(len(e)) :
        e_np += [[0] * (3-len(e[i])) + e[i]]
        but_np += [[0] * (3-len(but[i])) + but[i]]

    but_np = np.array(but)
    e_np = np.array(e)
    for i in range(len(e)) :
        for j in range(len(e[0])) :
            if e[i][j] != 0 :
                res+= abs(np.where(but_np==e_np[i][j])[0][0] - i) + abs(np.where(but_np==e_np[i][j])[0][1] - j)
    return res

def heuristique(g,h) :
    return g+h

from collections import deque

def ProfondeurBornee(seuil,etat) :
    nSeuil = float('inf')
    vus = {}
    enAttente = deque([(etat, [etat])])

    while enAttente :
        prochain, chemin = enAttente.pop()
        prochain_tuple = tuple(map(tuple, prochain))
        if estBut(prochain) :
            vus[prochain_tuple] = True
            return chemin 
        else :
            vus[prochain_tuple] = True
            for e in opPos(prochain):
                e_tuple = tuple(map(tuple, e[1]))
                h = profondeurMalPlace(e[1])
                if(e_tuple not in vus and h <= seuil[0]) :
                    enAttente.appendleft((e[1], chemin + [e[1]]))
                else :
                    nSeuil = min(nSeuil,h)
        
    if(nSeuil == float('inf')) : return chemin
    else :
        seuil[0] = nSeuil
        return []

def IDAstar(init):
    seuil = [profondeurMalPlace(init)]
    while True:
        solution = ProfondeurBornee(seuil, init)
        if solution:
            return solution
        elif not seuil[0] < float('inf'):
            return None


RumbaGame_1 = [[2,3],[1],[4,5,6],[7,8,9]]
RumbaGame_2 = [[1,2,3],[4,5,6],[7,8,9],[]]

but_1 = [[1,2,3],[],[4,5,6],[7,8,9]]
but_2 = [[1,2,3],[9,8,7],[4,5,6],[]]
but_3 = [[7,2,3],[8,4,6],[1,5,9],[]]
but_4 = [[2,1,3],[5,4,6],[8,7,9],[]]
but_5 = [[8,2,3],[4,6],[5,7,9],[1]]
but_6 = [[1,7,4],[2,8,5],[3,9,6],[]]

but = but_6
RumbaGame = RumbaGame_1

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
if res :
    for e in res :
        afficherEtat(e)
    print(len(res))
else : 
    print("Echec de la resolution" )