import java.security.KeyStore;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) {
        //System.out.println("숫자 입력");

        //Scanner s = new Scanner(System.in);
        //int input = s.nextInt();

        //for (int i = s.nextInt(); i < input; i++) {
        //System.out.println(i);

        //System.out.println("크기 입력");

        Scanner sc = new Scanner(System.in);
        //int input = sc.nextInt();

        //for (int i = 0; i < input; i++) {

            //for (int j = 0; j < input; j++) {
                //System.out.print("*");
            //}
            //System.out.println();
        //}

        //boolean money = true;

        //if (money) {
            //Syst

        int score = sc.nextInt();
        
        if (score >= 90 && score <= 100) {
            System.out.println('A');
        } else if (80 <= score && score < 90) {
            System.out.println('B');
        } else if (70 <= score && score < 80) {
            System.out.println('C');
        } else if (60 <= score && score < 70) {
            System.out.println('D');
        } else System.out.println('F');
        }
    }