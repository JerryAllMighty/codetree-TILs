import java.util.*;

public class Main {
    static String getSeason(int month) {
        String season = "";
        switch (month) {
            case 3:
                season = "Spring";
                break;
            case 4:
                season = "Spring";
                break;
            case 5:
                season = "Spring";
                break;
            case 6:
                season = "Summer";
                break;
            case 7:
                season = "Summer";
                break;
            case 8:
                season = "Summer";
                break;
            case 9:
                season = "Fall";
                break;
            case 10:
                season = "Fall";
                break;
            case 11:
                season = "Fall";
                break;
            case 12:
                season = "Winter";
                break;
            case 1:
                season = "Winter";
                break;
            case 2:
                season = "Winter";
                break;
            default:
                season = "";
        }

        return season;
    }

    static boolean isYoon(int year) {
        boolean isYoon = false;
        if (year % 4 == 0) {
            isYoon = true;
        } else if ((year % 4 == 0 && year % 100 == 0)) {
            if (year % 400 == 0) {
                isYoon = true;
            } else {
                isYoon = false;
            }
        } else {
            isYoon = false;
        }
        return isYoon;
    }

    static boolean isExistDate(int year, int month, int day) {
        boolean result = true;
        int limitDay = 0;
        boolean isYoon = isYoon(year);
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
                result = false;
        }
        if (isYoon) {
            limitDay = 29;
        }
        if (day < 0 || day > limitDay) {
            result = false;
        }
        return result;

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int year = Integer.parseInt(input[0]);
        int month = Integer.parseInt(input[1]);
        int day = Integer.parseInt(input[2]);
        boolean isExistDate = isExistDate(year, month, day);
        if (isExistDate) {
            String season = getSeason(month);
            System.out.println(season);
        } else {
            System.out.println(-1);
        }

        sc.close();
    }
}


