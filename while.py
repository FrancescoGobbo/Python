contatore=0
while True:
    contatore+=1
    if contatore==10:
        print("Salto il 10")
        continue
    print(contatore)
    if contatore>10:
        print("Sto uscendo dal loop!")
        break
