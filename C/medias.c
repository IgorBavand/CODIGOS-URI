#include <stdio.h>

int main() {
    int n = 0, cont = 0, i = 0;
    
    
    int vetor[10];
    for(i = 0; i < 10; i++){
        printf("digite o %d valor: ", i+1);
        int aux;
        scanf("%d", &aux);
        vetor[i] = aux;
    }
    printf("Qual numero vc deseja buscar? \n");
    scanf("%d", &n);

    for(i = 0; i < 10; i++){
        if(n == vetor[i]){
            cont++;
        }
    }

    printf("O valor %d aparece %d vez(es)\n", n,cont);

    return 0;
}