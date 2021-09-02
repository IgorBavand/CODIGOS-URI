#include<iostream>

using namespace std;

int main() { int n,num,i=0,aux1=0,aux2=0,aux=0,contador=0,pBase=0;

do{
    cin>>n;

    if(n != 0){

        cout<<"Discarded cards: ";  
        int pilhaCartas[n];
        aux2 = n;
        for(aux=0; aux<n;aux++){
            pilhaCartas[aux] = aux2;
            aux2--;
            contador++;
        }

        contador--;
        while(contador >= 1){

            if(contador == 1)
                cout<<pilhaCartas[contador];
            else
                cout<<pilhaCartas[contador]<<", ";  
            pilhaCartas[contador] = -1;
            pBase = pilhaCartas[contador-1];
            for(i=contador-1; i>0;i--){
                pilhaCartas[i] = pilhaCartas[i-1];
            }
            pilhaCartas[0]=pBase;
            contador--;
        }
        cout<<endl;

        cout<<"Remaining card: "<<pilhaCartas[0];
        cout<<endl;
    }   
}while(n !=0);
return 0;

}