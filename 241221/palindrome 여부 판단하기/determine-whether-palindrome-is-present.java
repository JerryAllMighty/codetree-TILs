import java.util.*;

public class Main {
    static boolean isPalindrome(String input) {
        String palindrome = "";
        for(int i = input.length()-1; i >= 0; i--){
            palindrome += input.substring(i, i+1);
        }
        return input.equals(palindrome);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        boolean isPalindrome = isPalindrome(input);
        if (isPalindrome) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}


