#include <stdio.h>

long long int soma(long long a, long long b){
    return a+b;
}

long long int multiplicacao(long long a, long long b){
    return a*b;
}

int main(){

    long long int n = 0;
    long long int p = 0, q = 0, res = 0;

    char c[2];

    scanf("%lld", & n);
    scanf("%lld %c %lld", &p, c, &q);

    if(c[0] == '+'){
        res = soma(p,q);
    }else{
        res = multiplicacao(p,q);
    }

    if(res > n){
        printf("OVERFLOW\n");
    }else{
        printf("OK\n");
    }

    return 0;
}