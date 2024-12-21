import java.util.*;

public class Main {
    static String calc(Integer a, Integer b) {
        if(a > b){
            b = b + 10;
            a = a * 2;
        }else{
            a = a + 10;
            b = b *2;
        }
        String[] arr = new String[2];
        arr[0] = Integer.toString(a);
        arr[1] = Integer.toString(b);
        return String.join(" ", arr);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        String calcList = calc(a, b);
        System.out.println(calcList);
//        System.out.println(String.join(" ",));

    }
}


