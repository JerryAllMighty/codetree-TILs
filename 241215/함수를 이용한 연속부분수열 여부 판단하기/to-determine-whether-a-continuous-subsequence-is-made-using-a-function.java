import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int n1 = Integer.parseInt(input[0]);
        int n2 = Integer.parseInt(input[1]);
        String[] n1List = sc.nextLine().split(" ");
        String[] n2List = sc.nextLine().split(" ");
        List<Integer> idxList = new ArrayList<>();
        for (int i = 0; i < n2; i++) {
            for (int j = 0; j < n1; j++) {
                if (Objects.equals(n1List[j], n2List[i])) {
                    idxList.add(j);
                }
            }
        }
        String answer = "Yes";
        for (int i = 0; i < idxList.size() - 1; i++) {
            if (idxList.get(i) + 1 != idxList.get(i + 1)) {
                answer = "No";
            }
        }
        if (idxList.isEmpty()) {
            answer = "No";
        }
        System.out.println(answer);

        sc.close();
    }
}

