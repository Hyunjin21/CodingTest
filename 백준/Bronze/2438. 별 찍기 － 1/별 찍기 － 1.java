import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        String str = "*";
        for(int i=1; i<=N; i++){
            System.out.println(str.repeat(i));   
        }
    scanner.close();
    }
}