def riempi_inventario():
    inventario=[]
    while True:
        oggetto= input("Cosa vuoi aggiungere nell'inventario?")
        if oggetto=="terminato":
            break
        else:
            inventario.append(oggetto)

    print("Gli oggetti presenti nell'inventario sono:\n" + str(inventario))

riempi_inventario()
