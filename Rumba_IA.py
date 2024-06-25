def afficherEtat(elt):
    maxi = max(len(sublist) for sublist in elt)
    for level in range(maxi - 1, -1, -1):
        print("                            ",end="")
        for pipe in elt:
            if level < len(pipe) : print(pipe[-level-1], end=" ")
            else : print(" ", end=" ")
        print("")
    print("-"*(len(elt)*18))

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
                res.append(((i+1, j+1), etat, 1))
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

def ProfondeurBornee(etat,but,g,seuil,chemin,mouvement) :
    f = g + profondeurMalPlace(etat[1],but)

    if f > seuil :
        return f
    
    if estBut(etat[1],but) :
        chemin.append(etat[1])
        mouvement.append(etat[0])
        return True
    
    nSeuil = float('inf')
    chemin.append(etat[1])
    mouvement.append(etat[0])
    for e in opPos(etat[1]) :
        if e[1] not in chemin :
            trouve = ProfondeurBornee(e,but,g+e[2],seuil,chemin,mouvement)
            if trouve == True : 
                if len(chemin) == 1 : 
                    chemin.append(e[1])
                    mouvement.append(e[0])
                return True
            if trouve < nSeuil : nSeuil = trouve
    chemin.remove(etat[1])
    mouvement.pop()
    
    return nSeuil

def IDAStar(init,but,nbIteration) :
    seuil = profondeurMalPlace(init,but)
    mouvement = []
    chemin = []
    init = ((0,0),init,0)

    while True :
        nbIteration[0]+=1
        trouve = ProfondeurBornee(init,but,0,seuil,chemin,mouvement)
        if trouve == True : return chemin,mouvement
        elif trouve == float('inf') : return [],[]
        else : seuil = trouve

def resoudre(init,but) :
    nbIteration = [0]
    res = IDAStar(init,but,nbIteration)
    if res[0] :
        for e in range(len(res[0])) :
            if e != 0 : print("Etape "+str(e)+ " : On déplace l'élement au sommet de la tour "+str(res[1][e][0])+" sur la tour "+str(res[1][e][1])) 
            else : print("Etat initial :")
            afficherEtat(res[0][e])
        print("Le problème a été résolu en "+str(len(res[0])-1)+" étape(s) avec "+str(nbIteration[0])+" parcour(s) en profondeur")
    else : 
        print("Echec de la resolution")

############## Valeurs pour tests ##############
RumbaGame_1 = [[2,3],[1],[4,5,6],[7,8,9]]
RumbaGame_2 = [[1,2,3],[4,5,6],[7,8,9],[]]

but_1 = [[1,2,3],[],[4,5,6],[7,8,9]]
but_2 = [[1,2,3],[9,8,7],[4,5,6],[]]
but_3 = [[7,2,3],[8,4,6],[1,5,9],[]]
but_4 = [[2,1,3],[5,4,6],[8,7,9],[]]
but_5 = [[8,2,3],[4,6],[5,7,9],[1]]
but_6 = [[1,7,4],[2,8,5],[3,9,6],[]]
################################################

resoudre(RumbaGame_2,but_6)