import java.util.*;

public class Main {
    public static int[] globalList;

    public static void recursive(int n) {
        if (n == 0) {
            return;
        }
        recursive(n - 1);
        System.out.println("HelloWorld");

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        recursive(n);


    }
}


