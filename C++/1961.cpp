#include<stdio.h>

int main(){

    int pulo = 0, qtd = 0, i = 0;

    scanf("%d %d", &pulo, &qtd);
    int torres[qtd];

    for(i = 0; i < qtd; i++){
        int aux;
        scanf("%d", &aux);
        torres[i] = aux;
    }

    int tam = qtd-2;
    int verifica = 1;
    int l = 0;

    while(l <= tam){
        if(torres[l+1] > torres[l]){
            if ((torres[l]+pulo) < torres[l+1])
                verifica = 0;
        }else{
            if ((torres[l+1]+pulo) < torres[l])
                verifica = 0;   
        }
    
        l++;
    }

    if(verifica == 1){
        puts("YOU WIN");
    }else{
        puts("GAME OVER");
    }

    return 0;
}