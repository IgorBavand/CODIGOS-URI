#include<iostream>

using namespace std;

int main(){
    int n = 0, d = 0;
    
    while(true){
        cin >> n >> d;
        if(n==0&&d==0)break;
        int matriz[d][n];
        int verifica = 0;

        //PREENCHENDO A MATRIZ
        for(int i = 0; i < d;i++){   
            for(int l = 0; l < n;l++){
                cin >> matriz[i][l];
            }
        }

        //VERIFICA POR COLUNAS  
        for(int i = 0; i < n;i++){   
            int cont = 0;
            for(int l = 0; l < d;l++){
                if(matriz[l][i] == 1){
                    cont++;
                }
            }
             if(cont == d){
                verifica++;
            }
           
        }
        if(verifica != 0) cout << "yes"<< endl;
        if(verifica == 0) cout << "no"<< endl;

    }
    return 0;
}