import java.util.*;

public class Main {
    static class IntWrapper{
        int val = 0;

        IntWrapper(int a){
            this.val = a;

        }
    }
    static void calc(IntWrapper a, IntWrapper b) {
        if(a.val > b.val){
            b.val += 10;
            a.val *= 2;
        }else{
            a.val += 10;
            b.val *= 2;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        IntWrapper intA = new IntWrapper(a);
        IntWrapper intB = new IntWrapper(b);
        calc(intA, intB);
        input[0] = Integer.toString(intA.val);
        input[1] = Integer.toString(intB.val);
        System.out.println(String.join(" ",input));
//        System.out.println(String.join(" ",));

    }
}


