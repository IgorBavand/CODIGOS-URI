import java.util.Scanner;


public class App {
    public static void main(String[] args) throws Exception {
        while(true){
            int n = 0;
            Scanner entrada = new Scanner(System.in);
            n = entrada.nextInt();
            if(n==0)break;

            int i = 1, l = 1, aux1 = 1, aux2 = 1;   
            while(i <= n){  
                
                l = 1;
                while(l <= n){
                    System.out.print(aux2+" ");
                    aux2 = aux2*2;
                    l++;
                }
                System.out.println();
                aux1 = aux1 * 2;
                aux2 = aux1;
                i++;                
            }

        }


    }
}
