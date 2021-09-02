#include<iostream>

using namespace std;

int main(){

    while(true){

        int n = 0;
        cin >> n;
        if(n==0)break;

        int i = 1, l = 1, aux1 = 1, aux2 = 1;   
            while(i <= n){  
                
                l = 1;
                while(l <= n){
                    cout << aux2 << " ";
                    aux2 = aux2*2;
                    l++;
                }
                cout << endl;
                aux1 = aux1 * 2;
                aux2 = aux1;
                i++;                
            }

    }

    return 0;
}