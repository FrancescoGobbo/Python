def reverser(stringa):
    indice=(len(stringa)-1)
    nuova_stringa=""
    while indice>=0:
        nuova_stringa+=stringa[indice]
        indice-=1
    print(nuova_stringa)

alfa="supercalifragilistichespiralidoso"

reverser(alfa)
