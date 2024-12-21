import java.util.*;

public class Main {
    static void modify(String[] lst) {
        for (int i = 0; i < lst.length; i++) {
            int toInt = Integer.parseInt(lst[i]);
            if (toInt % 2 == 0) {
                lst[i] = Integer.toString(toInt / 2);
            }
        }
        String result = String.join(" ",lst);
        System.out.println(result);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String  a = sc.nextLine();
        String[] input = sc.nextLine().split(" ");
        modify(input.clone());
    }
}


