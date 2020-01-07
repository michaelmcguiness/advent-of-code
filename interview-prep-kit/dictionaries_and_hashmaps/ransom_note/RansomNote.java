import java.util.*;

public class RansomNote {

    // Complete the checkMagazine function below.
    static void checkMagazine(String[] magazine, String[] note) {
        HashMap<String, Integer> map = new HashMap<>();

        // populate hashmap with words in magazine
        for (int i = 0; i < magazine.length; i++) {
            if (map.containsKey(magazine[i])) {
                map.replace(magazine[i], map.get(magazine[i]) + 1);
            } else {
                map.put(magazine[i], 0);
            }
        }

        // check words from note
        for (int i = 0; i < note.length; i++) {
            if (map.containsKey(note[i])) {
                if (map.get(note[i]) < 0) {
                    System.out.println("No");
                    return;
                } else {
                    map.replace(note[i], map.get(note[i]) - 1);
                }
            } else {
                System.out.println("No");
                return;
            }
        }
        System.out.println("Yes");
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] mn = scanner.nextLine().split(" ");

        int m = Integer.parseInt(mn[0]);

        int n = Integer.parseInt(mn[1]);

        String[] magazine = new String[m];

        String[] magazineItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < m; i++) {
            String magazineItem = magazineItems[i];
            magazine[i] = magazineItem;
        }

        String[] note = new String[n];

        String[] noteItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            String noteItem = noteItems[i];
            note[i] = noteItem;
        }

        checkMagazine(magazine, note);

        scanner.close();
    }
}
