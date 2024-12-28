import java.util.*;

public class Main {
    public static int[] globalList;

    public static void calc(String[] pair) {
        int result = 0;
        int startIdx = Integer.parseInt(pair[0]);
        int lastIdx = Integer.parseInt(pair[pair.length - 1]);
        for (int i = startIdx; i <= lastIdx; i++) {
            result += globalList[i - 1];
        }

        System.out.println(result);

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        globalList = new int[n];
        int m = Integer.parseInt(input[1]);
        String[] givenList = sc.nextLine().split(" ");
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(givenList[i]);
            globalList[i] = num;
        }
        for (int j = 0; j < m; j++) {
            String[] pair = sc.nextLine().split(" ");
            calc(pair);
        }


    }
}


