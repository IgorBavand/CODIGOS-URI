paises = ['brasil','alemanha','austria','coreia','espanha','grecia','estados-unidos','inglaterra','australia','portugal','suecia','turquia','argentina','chile','mexico','antardida','canada','irlanda','belgica','italia','libia','siria','marrocos','japao']

idiomas = ['Feliz Natal!','Frohliche Weihnachten!','Frohe Weihnacht!','Chuk Sung Tan!','Feliz Navidad!','Kala Christougena!','Merry Christmas!','Merry Christmas!','Merry Christmas!','Feliz Natal!','God Jul!','Mutlu Noeller!','Feliz Navidad!','Feliz Navidad!','Feliz Navidad!','Merry Christmas!','Merry Christmas!','Nollaig Shona Dhuit!','Zalig Kerstfeest!','Buon Natale!','Buon Natale!','Milad Mubarak!','Milad Mubarak!','Merii Kurisumasu!']

while True:
    try:
        pais = input()
        if pais in paises:
            print(idiomas[paises.index(pais)])
        else:
            print('--- NOT FOUND ---')


    except:
        break