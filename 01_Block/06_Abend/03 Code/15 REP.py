def begrussung(name,formell = True):
    if formell == True:
       print("Guten Tag, " + name)
    elif formell == False:
       print("Hoi, " + name)


#Test
begrussung("Anna")
begrussung("Ben",formell=False)