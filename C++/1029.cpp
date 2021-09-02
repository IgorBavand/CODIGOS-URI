#include<iostream>

using namespace std;

int cont = 0;

int fib(int n){
    cont++;
    
    if(n == 1){
        return 1;
    }else if(n == 0){
        return 0;
    }else{
        return fib(n-1)+fib(n-2);
       
    }
   
}

int main(){
    int qtd_entradas = 0;
    cin >> qtd_entradas;
    for(int i = 1; i <= qtd_entradas; i++){
        int n = 0;
        int res = 0;
        cin >> n;
        cont = 0;
        res = fib(n);
        cout << "fib(" <<n<< ")" << " = " << cont-1 << " calls" << " = " << res<<endl;

        //fib(4) = 8 calls = 3
        
    }

    return 0;
}