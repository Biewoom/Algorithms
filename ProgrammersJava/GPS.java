import java.util.*;

public class GPS {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = Integer.parseInt(sc.nextLine());
    int m = Integer.parseInt(sc.nextLine());

    int[][] edge_list = new int[m][2];
    String tmpLine = sc.nextLine();
    String[] tmp = tmpLine.substring(1, tmpLine.length() - 1).split("\\],\\[");
    for (int i = 0; i < tmp.length; i++) {
      String[] tt = tmp[i].split(", ");
      edge_list[i][0] = Integer.parseInt(tt[0]);
      edge_list[i][1] = Integer.parseInt(tt[1]);
    }

    int k = Integer.parseInt(sc.nextLine());

    int[] gps_log = new int[k];
    String tempLine = sc.nextLine();
    String[] temp = tempLine.substring(1, tempLine.length() - 1).split(", ");
    for (int i = 0; i < temp.length; i++) {
      gps_log[i] = Integer.parseInt(temp[i]);
    }

    int answer = new Solution().solution(n, m, edge_list, k, gps_log);
    System.out.println(answer);
    sc.close();
  }
}

class Solution {

  public void initializeDP(int[][] dp, int inf) {
    for (int r = 0; r < dp.length; r++) {
      Arrays.fill(dp[r], inf);
    }
  }

  public void initializeEdgeMap(int[][] edge_list,
                                Map<Integer, ArrayList<Integer>> edgeMap) {
    for (int i = 0; i < edge_list.length; i++) {
      int v1 = edge_list[i][0];
      int v2 = edge_list[i][1];

      if (edgeMap.get(v1) == null)
        edgeMap.put(v1, new ArrayList<Integer>());
      if (edgeMap.get(v2) == null)
        edgeMap.put(v2, new ArrayList<Integer>());

      edgeMap.get(v1).add(v2);
      edgeMap.get(v2).add(v1);
    }
  }
  public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
    final int INF = 100000;
    int Min = INF;

    Map<Integer, ArrayList<Integer>> edgeMap =
        new Hashtable<Integer, ArrayList<Integer>>();
    initializeEdgeMap(edge_list, edgeMap);

    int[][] dp = new int[k][n + 1];
    initializeDP(dp, INF);

    int start = gps_log[0];
    int end = gps_log[k - 1];
    dp[0][start] = 0;

    for (int index = 0; index < k - 1; index++) {

      for (int node = 1; node < n + 1; node++) {
        if (dp[index][node] == INF)
          continue;

        ArrayList<Integer> nextCandidates = new ArrayList<>(edgeMap.get(node));
        nextCandidates.add(node);

        for (int nextNode : nextCandidates) {
          int value = dp[index][node];

          if (nextNode != gps_log[index + 1])
            value++;

          dp[index + 1][nextNode] = Math.min(dp[index + 1][nextNode], value);
        }
      }
    }
    return ((dp[k - 1][end] != INF) ? dp[k - 1][end] : -1);
  }
}
