x=15 #variabile globale

def funzione_esempio():
    y=2 #variabile locale
    global x    #modifica variabile globale
    x+=2
    y+=2
    return (y)

print(funzione_esempio())

def funzione_esempio():
    y=x #variabile locale
    y+=2
    return (y)

print(funzione_esempio())

def mia_funzione():
    spam=24
    return spam
eggs= mia_funzione()+6
print(eggs)
