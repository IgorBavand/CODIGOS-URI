import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner entrada = new Scanner(System.in);
        int n = 0, l = 0;
        int vetor[];
        vetor = new int[1000];

        n = entrada.nextInt();


        for(int i = 0; i < 1000; i++){
            if(l>=n)l=0;
            vetor[i] = l; 
            l++;
        }


        for(int i = 0; i < 1000; i++){
           System.out.println("N"+"["+i+"]"+" = "+vetor[i]);
        }
        
    }
}
