#include<iostream>

using namespace std;

int main(){

    int n = 0;
    int vetor[10];
    int l = 0;
    cin >> n;

    for(int i = 0; i < 10; i++){
        
        while(l < n){
            //vetor[i] = l;
            cout << l <<endl;
            l++;
        }
    }

    for(int i = 0; i < 10; i++){
        //cout << vetor[i]<<endl;
    }

    return 0;
}