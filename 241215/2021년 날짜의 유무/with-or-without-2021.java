import java.util.*;

public class Main {
    static String isExistDate(int month, int day) {
        String result = "Yes";
        int limitDay = 0;
        switch (month) {
            case 1:
                limitDay = 31;
                break;
            case 3:
                limitDay = 31;
                break;
            case 5:
                limitDay = 31;
                break;
            case 7:
                limitDay = 31;
                break;
            case 8:
                limitDay = 31;
                break;
            case 10:
                limitDay = 31;
                break;
            case 12:
                limitDay = 31;
                break;
            case 4:
                limitDay = 30;
                break;
            case 6:
                limitDay = 30;
                break;
            case 9:
                limitDay = 30;
                break;
            case 11:
                limitDay = 30;
                break;
            case 2:
                limitDay = 28;
                break;
            default:
                result = "No";
        }
        if (day < 0 || day > limitDay) {
            result = "No";
        }
        return result;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int month = Integer.parseInt(input[0]);
        int day = Integer.parseInt(input[1]);
        String result = isExistDate(month, day);
        System.out.println(result);
        sc.close();
    }
}


