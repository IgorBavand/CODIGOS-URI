import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        int p = 0, contador = 0;

        Scanner entrada = new Scanner(System.in);
        p = entrada.nextInt();
        
        String digitos = ""; 
        
        for(int i = 1; i <= p; i++){
            digitos = Integer.toString(i);
            contador = contador + digitos.length();
        }

        System.out.println(contador);
        entrada.close();
    }
    
}
