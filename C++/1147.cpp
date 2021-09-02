#include<iostream>

using namespace std;

char verifica_pos(char n){
    if(n == 'a'){
        return '1';
    }if(n == 'b'){
        return '2';
    }if(n == 'c'){
        return '3';
    }if(n == 'd'){
        return '4';
    }if(n == 'e'){
        return '5';
    }if(n == 'f'){
        return '6';
    }if(n == 'g'){
        return '7';
    }if(n == 'h'){
        return '8';
    }
}

int main(){

    char tabuleiro[8][8];
    
        for(int i = 0; i < 8;i++){
            for(int l = 0; l < 8; l++){
                tabuleiro[i][l] = ' ';
            }
        }
    int l1,c1,l2,c2,l3,c3,l4,c4,l5,c5,l6,c6,l7,c7,l8,c8;

    char entrada1[3],entrada2[3],entrada3[3],entrada4[3],entrada5[3],entrada6[3],entrada7[3],entrada8[3];
    char pos_cavalo[3];
    cin >> pos_cavalo;

    cin >> entrada1;
    l1 = (int)entrada1[0];
    c1 = (int)verifica_pos(entrada1[1]) - 48;
    tabuleiro[l1][c1] = 'P';

    cin >> entrada2;
    l2 = (int)entrada2[0];
    c2 = (int)verifica_pos(entrada2[1]) - 48;
    tabuleiro[l2][c2] = 'P';

    cin >> entrada3;
    l3 = (int)entrada3[0];
    c3 = (int)verifica_pos(entrada3[1]) - 48;
    tabuleiro[l3][c3] = 'P';

    cin >> entrada4;
    l4 = (int)entrada4[0];
    c4 = (int)verifica_pos(entrada4[1]) - 48;
    tabuleiro[l4][c4] = 'P';

    cin >> entrada5;
    l5 = (int)entrada5[0];
    c5 = (int)verifica_pos(entrada5[1]) - 48;
    tabuleiro[l5][c5] = 'P';

    cin >> entrada6;
    l6 = (int)entrada6[0];
    c6 = (int)verifica_pos(entrada6[1]) - 48;
    tabuleiro[l6][c6] = 'P';

    cin >> entrada7;
    l7 = (int)entrada7[0];
    c7 = (int)verifica_pos(entrada7[1]) - 48;
    tabuleiro[l7][c7] = 'P';


    cin >> entrada8;
    l8 = (int)entrada8[0];
    c8 = (int)verifica_pos(entrada8[1]) - 48;
    tabuleiro[l8][c8] = 'P';


    

    for(int i = 0; i < 8;i++){
        for(int l = 0; l < 8; l++){
            cout << tabuleiro[i][l] << " ";
        }
        cout <<endl;
    }

    

    return 0;
}