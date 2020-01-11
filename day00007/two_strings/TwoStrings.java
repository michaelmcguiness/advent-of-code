import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class TwoStrings {

    static HashMap<Character, Integer> convertToMap(String s) {
        HashMap<Character, Integer> myMap = new HashMap<>();
        for (int i = 0, n = s.length(); i < n; i++) {
            myMap.put(s.charAt(i), myMap.containsKey(s.charAt(i)) ? myMap.get(s.charAt(i)) + 1 : 1);
        }
        return myMap;
    }

    // Complete the twoStrings function below.
    static String twoStrings(String s1, String s2) {
        HashMap<Character, Integer> s1Map = convertToMap(s1);
        HashMap<Character, Integer> s2Map = convertToMap(s2);

        for (Map.Entry mapElement : s1Map.entrySet()) {
            char key = (char) mapElement.getKey();
            if (s2Map.containsKey(key)) {
                return "YES";
            }
        }
        return "NO";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s1 = scanner.nextLine();

            String s2 = scanner.nextLine();

            String result = twoStrings(s1, s2);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
