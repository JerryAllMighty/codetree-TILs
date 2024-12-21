import java.util.*;

public class Main {
    static String moreThanTwo(String s) {
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            String str = s.substring(i, i + 1);
            Integer val = map.get(str);
            if (val == null) {
                map.put(str, 1);
            } else {
                if (val + 1 >= 2) {
                    map.put(str, val + 1);
                }
            }
        }
        int mapKeySize = map.keySet().size();
        if(mapKeySize < 2){
            return "No";
        }else{
            return "Yes";
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String isMoreThanTwo = moreThanTwo(a);
        System.out.println(isMoreThanTwo);


    }
}


