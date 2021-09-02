n = int(input())

for i in range(n):
    palavra = input()
    palavra = list(palavra)
    cont = 0
    if 'a' in palavra:
        cont +=1
    if 'b' in palavra:
        cont +=1
    if 'c' in palavra:
        cont +=1
    if 'd' in palavra:
        cont +=1
    if 'e' in palavra:
        cont +=1
    if 'f' in palavra:
        cont +=1
    if 'g' in palavra:
        cont +=1
    if 'h' in palavra:
        cont +=1
    if 'i' in palavra:
        cont +=1
    if 'j' in palavra:
        cont +=1
    if 'k' in palavra:
        cont +=1
    if 'l' in palavra:
        cont +=1
    if 'm' in palavra:
        cont +=1
    if 'n' in palavra:
        cont +=1
    if 'o' in palavra:
        cont +=1
    if 'p' in palavra:
        cont +=1
    if 'q' in palavra:
        cont +=1
    if 'r' in palavra:
        cont +=1
    if 's' in palavra:
        cont +=1
    if 't' in palavra:
        cont +=1
    if 'u' in palavra:
        cont +=1
    if 'v' in palavra:
        cont +=1
    if 'w' in palavra:
        cont +=1
    if 'x' in palavra:
        cont +=1
    if 'y' in palavra:
        cont +=1
    if 'z' in palavra:
        cont +=1

    if cont == 26:
        print('frase completa')
    if cont >= 13 and cont < 26:
        print('frase quase completa')
    if cont < 13:
        print('frase mal elaborada')

