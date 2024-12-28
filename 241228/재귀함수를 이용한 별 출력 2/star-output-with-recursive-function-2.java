import java.util.*;


public class Main {
    public static int[] globalList;

    public static void recursive(int n) {
        if (n == 0) {
            return;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append("* ");
        }
        sb.delete(2*n-1,2*n);
        System.out.println(sb);

        recursive(n - 1);

        StringBuilder sb2 = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb2.append("* ");
        }
        sb2.delete(2*n-1,2*n);
        System.out.println(sb2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        recursive(n);


    }
}


