import java.util.Scanner;


public class App {
    public static void main(String[] args) throws Exception {
        int[] vetor1;
        int[] vetor2;
        int cont = 0;

        Scanner entrada = new Scanner(System.in);

        vetor1 = new int[5];
        vetor2 = new int[5];

        for(int i = 0; i < 5; i++){
            vetor1[i] = entrada.nextInt();
        }
        for(int i = 0; i < 5; i++){
            vetor2[i] = entrada.nextInt();
        }
        for(int i = 0; i < 5; i++){
            if(vetor1[i] == vetor2[i]){
                cont++;
            }
        }

        if(cont == 0) System.out.println("Y"); else System.out.println("N"); 
        

        entrada.close();

    }
}
