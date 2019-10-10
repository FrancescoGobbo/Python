e=input('Quale età hai?')
età=int(e)
possiede_patente=False;
patente=input('Hai la patente? (Si/No)')
if patente== 'Si':
    possiede_patente=True;
if età>=18 and possiede_patente==True:
    print("Sei maggiorenne e puoi guidare")
elif età>=18 and possiede_patente==False:
    print("Sei maggiorenne, ma non puoi guidare")
else:
    print("Sei minorenne")
