texto=input()
#texto = open('teste1667.txt', 'r')

#texto = str(texto)

texto = texto.replace('<hr>', '-'*80)
texto = texto.replace('<br>', '\n')

print(texto)