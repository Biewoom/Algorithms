package UserDefined;
import java.util.*;

public class ParsingString {
  public static void make2DIntArray(String Line, int[][] arr) {
    int m = arr.length;
    int n = arr[0].length;

    String[] ll = Line.substring(1, Line.length() - 1).split("\\], \\[");
    for (int i = 0; i < m; i++) {
      String[] lll = ll[i].split(", ");
      for (int j = 0; j < n; j++) {
        arr[i][j] = Integer.parseInt(lll[j]);
      }
    }
  }
  public static void sayHello() {
    System.out.println("from ParsingString java");
  }
}
