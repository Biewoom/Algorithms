import java.util.*;

public class BlindMeetingWithTube {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int m = Integer.parseInt(sc.nextLine());
    int n = Integer.parseInt(sc.nextLine());
    int s = Integer.parseInt(sc.nextLine());

    int[][] time_map = new int[m][n];

    String L = sc.nextLine();
    String[] ll = L.substring(1, L.length() - 1).split("\\], \\[");

    for (int i = 0; i < m; i++) {
      String[] lines = ll[i].split(", ");
      for (int j = 0; j < n; j++) {
        time_map[i][j] = Integer.parseInt(lines[j]);
      }
    }

    System.out.println(
        Arrays.toString(new Solution().solution(m, n, s, time_map)));
    sc.close();
  }
}

class Solution {
  int[] dx = {0, 0, 1, -1};
  int[] dy = {1, -1, 0, 0};

  boolean safe(int x, int y, int m, int n) {
    if ((0 <= x) && (x < m) && (0 <= y) && (y < n))
      return true;
    else
      return false;
  }

  public int[] solution(int m, int n, int s, int[][] time_map) {
    int[] answer = new int[2];
    long[][][] dp = new long[52][52][2510];

    PriorityQueue<int[]> pq =
        new PriorityQueue<int[]>(10, new ArrayComparator());

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        Arrays.fill(dp[i][j], s + 1);
      }
    }
    dp[0][0][0] = 0;
    int[] start = {0, 0, 0}; //{curD, curX, curY}
    pq.add(start);

    while (pq.size() != 0) {
      int[] curArr = pq.poll();
      int curD = curArr[0];
      int curX = curArr[1];
      int curY = curArr[2];

      if (curD > (n * m))
        continue;
      if (dp[curX][curY][curD] > s)
        continue;

      for (int i = 0; i < 4; i++) {
        int newX = curX + dx[i];
        int newY = curY + dy[i];
        if (!safe(newX, newY, m, n))
          continue;
        if (time_map[newX][newY] == -1)
          continue;

        if ((dp[curX][curY][curD] + time_map[newX][newY]) <
            dp[newX][newY][curD + 1]) {
          int[] nextArr = {curD + 1, newX, newY};
          dp[newX][newY][curD + 1] =
              dp[curX][curY][curD] + time_map[newX][newY];
          pq.add(nextArr);
        }
      }
    }

    for (int d = 0; d < n * m; d++) {
      if (dp[m - 1][n - 1][d] <= s) {
        answer[0] = d;
        answer[1] = dp[m - 1][n - 1][d];
        break;
      }
    }
    return answer;
  }
}

class ArrayComparator implements Comparator<int[]> {
  public int compare(int[] a, int[] b) {
    return (((a[0] - b[0]) > 0) ? 1 : -1);
  }
}
