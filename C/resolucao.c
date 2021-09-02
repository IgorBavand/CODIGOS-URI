#include <stdio.h>


void imprimir(int n){
    for(int i = 1; i <= n; i++){
        for(int l = 1; l <= n; l++){
            if(l == 1 || i == 1 || l == n || i == n){
                printf("   1");
            }else{
                printf("   2");
            }
        }puts("");
    }puts("");
}

int main(){
    int n;
    
    while(1){
        scanf("%d", &n);
        if(n == 0) break;
        imprimir(n);
    }

    
   
}