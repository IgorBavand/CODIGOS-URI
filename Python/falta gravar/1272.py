while True:
    try:
        n = int(input())
        frase = input()
        palavras = []
        frase = frase.replace('.',' ')

        palavras = list(map(str, frase.input().split()))


        print(palavras)
    except EOFError:
        break