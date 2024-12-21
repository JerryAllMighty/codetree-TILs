import java.util.*;

public class Main {
    static void calc(int a, int b) {
        String answer = "";
        if (a > b) {
            answer += Integer.toString(a + 25) + " " + Integer.toString(b * 2);
        } else {
            answer += Integer.toString(a * 2) + " " + Integer.toString(b + 25);
        }
        System.out.println(answer);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        calc(a, b);

    }
}


