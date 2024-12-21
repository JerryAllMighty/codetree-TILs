import java.util.*;

public class Main {
    static void toAbs(String[] input) {
        String answer = "";
        for (int i = 0; i < input.length; i++) {
            int toInt = Integer.parseInt(input[i]);
            if (toInt < 0) {
                input[i] = Integer.toString(-toInt);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String[] input = sc.nextLine().split(" ");
        toAbs(input);
        System.out.println(String.join(" ", input));

    }
}


