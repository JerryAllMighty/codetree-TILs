import java.util.*;

public class Main {
    static boolean isSameArray(List<String> n1, String[] n2) {
        boolean result = true;
        for (int i = 0; i < n1.size(); i++) {
            if (!n1.get(i).equals(n2[i])) {
                return false;
            }
        }
        return result;
    }

    static List<String> makePartArray(String[] n1, int n, int m) {
        List<String> result = new ArrayList<>();
        for (int i = n; i < m; i++) {
            result.add(n1[i]);
        }
        return result;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int n1 = Integer.parseInt(input[0]);
        int n2 = Integer.parseInt(input[1]);
        String[] n1List = sc.nextLine().split(" ");
        String[] n2List = sc.nextLine().split(" ");
        String answer = "No";
        for (int i = 0; i <= n1 - n2; i++) {
            if (isSameArray(makePartArray(n1List, i, i + n2), n2List)) {
                answer = "Yes";
                System.out.println(answer);
                sc.close();
                System.exit(0);
            }
        }
        System.out.println(answer);
        sc.close();
    }
}

