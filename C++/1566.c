#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int getValor(char s[]){
    int t, nr, i;
    char snr[100];

    t = strlen(s);

    for (t--; s[t] != ' '; t--);

    for(t++, i=0; s[t] != '\0'; t++, i++)
        snr[i] = s[t];

    snr[i]= '\0';

    nr = atoi(snr);
    return nr;
}

void  retiraNumero(char s[]){
    int t = strlen(s);

    for(t--; s[t] != ' '; t--);

    s[t] = '\0';
}

int main(int argc, char** argv) {

    int casos=0, altura;
    int i, j;
    char titan[1000];
    int alt;
    char nomes[100];

    scanf("%d %d", &casos, &altura);

    for (i=0;i<casos;i++){
        fflush(stdin);
        gets(titan);

        alt = getValor(titan);

        retiraNumero(titan);

     if(alt>altura)
      printf("%s\n", titan);
    }

    return 0;
}