import java.util.*;

class Solution {
  static final int MOD = 20170805;
  public static int solution(int m, int n, int[][] cityMap) {
    int[][][] dp = new int[2][m + 1][n + 1];
    dp[0][0][0] = 1;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (cityMap[i][j] == 0) {
          dp[0][i + 1][j] = (dp[0][i + 1][j] + dp[0][i][j] + dp[1][i][j]) % MOD;
          dp[1][i][j + 1] = (dp[1][i][j + 1] + dp[0][i][j] + dp[1][i][j]) % MOD;
        } else if (cityMap[i][j] == 2) {
          dp[0][i + 1][j] = (dp[0][i + 1][j] + dp[0][i][j]) % MOD;
          dp[1][i][j + 1] = (dp[1][i][j + 1] + dp[1][i][j]) % MOD;
        } else {
          ;
        }
      }
    }

    return (dp[0][m - 1][n - 1] + dp[1][m - 1][n - 1]) % MOD;
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int m = Integer.parseInt(sc.nextLine());
    int n = Integer.parseInt(sc.nextLine());

    int[][] cityMap = new int[m][n];
    String line = sc.nextLine();
    String[] lines = line.substring(1, line.length() - 1).split("\\],\\[");

    for (int i = 0; i < m; i++) {
      String[] newLine = lines[i].split(", ");
      for (int j = 0; j < n; j++) {
        cityMap[i][j] = Integer.parseInt(newLine[j]);
      }
    }
    System.out.println("cityMap: " + Arrays.deepToString(cityMap));
    System.out.println(solution(m, n, cityMap));
  }
}
