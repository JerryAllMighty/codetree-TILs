import java.util.*;


public class Main {
    public static int[] globalList;

    public static void recursive(int n){
        if (n == 0) {
            return;
        }
        recursive(n - 1);
        System.out.printf(String.valueOf(n) + " ");
    }
    public static void recursive2(int n){
        if (n == 0) {
            return;
        }
        System.out.printf(String.valueOf(n) + " ");
        recursive2(n - 1);

    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        recursive(n);
        System.out.println();
        recursive2(n);


    }
}


