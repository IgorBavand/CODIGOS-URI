#include<iostream>

using namespace std;


int fib(int n){
    if(n == 0){
        return 0;
    }else if(n == 1){
        return 1;
    }else{
        return fib(n-1)+fib(n-2);
    }

}

int main(){
    int n = 0;
    cin >> n;
    for(int i = 0;i < n; i++){
        int x = 0;
        cin >> x;
        cout << "Fib(" << x << ") = " << fib(x)<<endl;
    }
    return 0;
}