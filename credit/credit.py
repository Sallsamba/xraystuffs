def credit(prix):
    taux=0.013
    soldes=120000
    pret=prix*(1+taux)
    if pret>=soldes:
        False
    else:
        duree=[12,24,36,48]
        mensualite_list=[]
        for men in duree:
            mensualite=pret/men
            mensualite_list.append(mensualite)

        return (duree,mensualite_list)

