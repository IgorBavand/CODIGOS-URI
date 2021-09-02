import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        double c = 0;
        double p = 0;
        int f = 0;


        
        Scanner teclado = new Scanner(System.in);
        
        c = Double.parseDouble(teclado.nextLine());
        p = Double.parseDouble(teclado.nextLine());
        
        

        double x = c+p;

        System.out.println("SOMA = "+x);


    }

    
}
