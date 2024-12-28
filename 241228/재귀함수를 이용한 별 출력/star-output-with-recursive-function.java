import java.util.*;


public class Main {
    public static int[] globalList;

    public static void recursive(int n) {
        if (n == 0) {
            return;
        }
        recursive(n - 1);
        StringBuilder star = new StringBuilder();
        for (int i = 0; i < n; i++) {
            star.append("*");
        }
        System.out.println(star);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        recursive(n);


    }
}


