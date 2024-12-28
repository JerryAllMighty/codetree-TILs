import java.util.*;


public class Main {
    public static int[] globalList;

    public static void recursive(int n) {
        if (n == 0) {
            return;
        }
        System.out.print(n + " ");
        recursive(n - 1);
        System.out.print(n + " ");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        recursive(n);


    }
}


