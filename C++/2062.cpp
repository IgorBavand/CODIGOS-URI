#include <stdio.h>
#include <string.h>

int main ()
{

  unsigned short palavras, i, tamanho;
  char palavra[30];
  
  scanf("%hu", &palavras);

  for ( i = 0; i < palavras; i++)
  {

    scanf("%s", palavra);
    tamanho = strlen(palavra);

    if (i != 0)
      printf(" ");
    if (tamanho == 3 && palavra[0] == 'O' && palavra[1] == 'B')
      printf("OBI");
    else if (tamanho == 3 && palavra[0] == 'U' && palavra[1] == 'R')
      printf("URI");
    else
      printf("%s", palavra);

  }
  printf("\n");
}