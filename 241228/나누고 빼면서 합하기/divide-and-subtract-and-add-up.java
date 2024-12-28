import java.util.*;

public class Main {
    public static int calc(int[] lst, int m) {
        int result = lst[m - 1];
        while (true) {
            if (m == 1) {
                break;
            } else {
                if (m % 2 != 0) {
                    m -= 1;
                    result += lst[m - 1];
                } else {
                    m /= 2;
                    result += lst[m - 1];
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        String[] givenList = sc.nextLine().split(" ");
        int cnt = Integer.parseInt(input[0]);
        int[] lst = new int[cnt];
        for (int i = 0; i < cnt; i++) {
            int num = Integer.parseInt(givenList[i]);
            lst[i] = num;
        }
        int m = Integer.parseInt(input[1]);
        int result = calc(lst, m);
        System.out.println(result);

    }
}


