#include<iostream>
#include<math.h>

using namespace std;

float calc_delta(float a, float b, float c){
    float delta = (b*b) - 4*a*c;
    return delta;
}

int main(){

    double a = 0.0, b = 0.0, c = 0.0;
    double r1 = 0.0, r2 = 0.0;
    cin >> a >> b >> c;

    double delta = calc_delta(a,b,c);

    

    if(delta <= 0 || a == 0){
        cout << "Impossivel calcular" << endl;
    }else{
        r1 = (-b+sqrt(delta))/2*a;
        r2 = (-b-sqrt(delta))/2*a;
        printf("R1 = %.5lf\n", r1/100);
        printf("R2 = %.5lf\n", r2/100);
        
    }
    return 0;
}