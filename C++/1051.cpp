#include<iostream>

using namespace std;

int main(){
    double valor = 0.0, percent = 0.0;

    cin >> valor;

    if(valor >= 0 && valor <= 2000.00){
        cout << "Isento" <<endl;
    }else if(valor >= 2000.01 && valor <= 3000.00){
        percent = 0.08*valor;
        printf("R$ %.2f\n", percent);
       
    }else if(valor >= 3000.01 && valor <= 4500.00){
        percent = 0.18*valor;
        printf("R$ %.2f\n", percent);
       
    }else{
        percent = 0.28*valor;
        printf("R$ %.2f\n", percent);
       
    }
    
   
    

    return 0;
}