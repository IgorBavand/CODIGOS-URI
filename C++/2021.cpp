#include<stdio.h>


int main(){


    bool veri = true;
    while(veri){
        int altura = 0, largura = 0, qtd_posicao = 0;

        scanf("%d %d %d", &altura, &largura, &qtd_posicao);
        
        if(altura == 0 && largura == 0 && qtd_posicao == 0) break;

        int cont = 0, posicao = 0, aux = 0, i = 1;

        for(i = 1; i <= qtd_posicao; i++){
                scanf("%d", &posicao);
                if(posicao <= largura){
                    cont = cont + (largura-posicao+1);
                }else{
                    aux = posicao-largura;
                    cont = cont + (largura-aux+1);
                }
                
        }

        if(cont < 0){
            cont = 1;
        }

        printf("Lights: %d\n", cont);
    }

    return 0;
}