# Ce programme permet de faire une proposition de crédit à client

from math import floor

def credit(prix):
    # taux et soldes fixés
    taux=0.013 
    soldes=15000
    # montant total
    pret=prix*(1+taux)
    # cas du montant insuffisant
    if pret>=soldes:
        return None

    # 4 propositions pour des durées différentes
    else:
        M=[]
        duree = [12,24,36,48]
        for men in duree:
            #calcul de la mensualité
            mensualite=floor(pret/men)
            M.append(mensualite)
        # retourne du résultat
        return "\n{}€x12, {}€x24, {}€*36, ou {}€*48 mensualités".format(M[0], M[1], M[2], M[3])

