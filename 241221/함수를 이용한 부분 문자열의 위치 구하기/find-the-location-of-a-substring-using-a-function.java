import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String word = sc.nextLine();
        int answer = -1;
        for (int i = 0; i <= input.length()-word.length(); i++) {
            String eachWord = input.substring(i, i + word.length());
            if (word.equals(eachWord)) {
                answer = i;
            }
        }
        System.out.println(answer);

    }
}


