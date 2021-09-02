#include<iostream>
#include<vector>

using namespace std;

class Coordenada{
    public:
        int x, y;
        bool visitada;
};

void buscar(vector< vector<int>> mat[5], vector< vector<Coordenada>> coordenadas[5], int i, int j){
    if(i >= 0 && i < 5 && j >= 0 && j < 5 && !winner){
        coordenadas[i][j].visitada = true;

        if(i == 4 && j == 4){
            winner = 1;
        }else{
            if(i + 1 < 5 && mat[i+1][j] == 0 && !coordenadas[i + 1][j].visitada){
                buscar(mat, coordenadas, i + 1, j);
            }if(i - 1 >= 0 && mat[i-1][j] == 0 && !coordenadas[i - 1][j].visitada){
                buscar(mat, coordenadas, i - 1, j);
            }if(j + 1 < 5 && mat[i][j + 1] == 0 && !coordenadas[i][j + 1].visitada){
                buscar(mat, coordenadas, i, j + 1);
            }if(j - 1 >= 0 && mat[i][j - 1] == 0 && !coordenadas[i][j - 1].visitada){
                buscar(mat, coordenadas, i, j - 1);
            }
        }
    }
}

int winner;

int main(int argc, char *argv[]){
    int t = 0, i = 0, j = 0, k = 0;
    cin >> t;

    for(i = 0; i < t;i++){

        vector<vector <int>> mat(5);
        vector<vector <Coordenada>> coordenadas(5);

        for(j = 0; j < 5; j++){
            mat[j].resize(5);
            coordenadas[j].resize(5);
        }



        for(j = 0;j < 5; j++){
            for(k = 0; k < 5; k++){
                int e = 0;
                cin >> e;
                mat[j][k] = e;

                coordenadas[j][k].x = j;
                coordenadas[j][k].y = k;

                coordenadas[j][k].visitada = false;
            }
        }

        winner = 0;
        buscar(mat, coordenadas, 0, 0);

        if(winner){
            cout << "COPS"<<endl;
        }else{
            cout << "ROBBERS"<<endl;
        }

    }

    return 0;
}