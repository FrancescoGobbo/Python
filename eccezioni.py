def divisione(a,b):
    while True:
        try:
            risultato=a/b
            print("Il risultato della divisione è: " + str(risultato))
        except ZeroDivisionError:
            print("Hei effettuato una divisione per Zero... ERRORE!!!")

        continua=input("Hai finito di dividere?  (S/N)")

        if continua=='N':
            k=int(input())
            j=int(input())
            a=k
            b=j
        else:
            break

def moltiplicazione():
    try:
        a=int(input("Scrivi il primo valore: "))
        b=int(input("Scrivi il secondo valore: "))
        risultato= a*b
        print(risultato)
    except ValueError:
        print("Sono accettati solo caratteri numerici")
    finally:
        print("Grazie per aver utilizzato questa applicazione")
