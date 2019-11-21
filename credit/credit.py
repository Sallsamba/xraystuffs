# Ce programme concerne à faire une proposition de crédit à client
# qui dépend de la durée


def credit(prix):
    # taux et soldes fixés
    taux=0.013 
    soldes=10000
    # montant total
    pret=prix*(1+taux)
    # cas du montant insuffisant
    if pret>=soldes:
        False

    # 4 propositions pour des durées différentes
    else:
        duree=[12,24,36,48]
        mensualite_list=[]
        for men in duree:
            #calcul de la mensualité
            mensualite=pret/men
            mensualite_list.append(mensualite)
        # retourne du résultat
        return (duree,mensualite_list)

