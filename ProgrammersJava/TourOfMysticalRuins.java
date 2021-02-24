import UserDefined.ParsingString;
import java.util.*;

public class TourOfMysticalRuins {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n1 = Integer.parseInt(sc.nextLine());
    int[][] g1 = new int[n1 - 1][2];
    ParsingString.make2DIntArray(sc.nextLine(), g1);
    int n2 = Integer.parseInt(sc.nextLine());
    int[][] g2 = new int[n2 - 1][2];
    ParsingString.make2DIntArray(sc.nextLine(), g2);
    System.out.println(new Solution().solution(n1, g1, n2, g2));
  }
}

class Solution {
  private static final int INF = 100000;
  ArrayList<Integer>[] children1;
  ArrayList<Integer>[] children2;

  private void initDP(int n, int m, int[][] dp, int[][] costDP,
                      int[][] flowDP) {

    int src = 0;
    int des = n + m + 1;

    // flowDP, costDP from src -> n
    for (int i = 0; i < n; i++) {
      int nIndex = i + 1;
      flowDP[0][nIndex] = 1;
      costDP[0][nIndex] = 0;
    }
    // flowDP, costDP from m -> des
    for (int i = 0; i < m; i++) {
      int mIndex = i + n + 1;
      flowDP[mIndex][des] = 1;
      costDP[mIndex][des] = 0;
    }
    // flowDP, costDP by referenc DP
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        int nIndex = i + 1;
        int mIndex = j + n + 1;

        // flowDP update
        flowDP[nIndex][mIndex] = 1;
        flowDP[mIndex][nIndex] = 0;
        // costDP update
        costDP[nIndex][mIndex] = dp[i][j] * -1;
        costDP[mIndex][nIndex] = dp[i][j];
      }
    }
  }

  private int MCMF(int n, int m, int[][] dp) {
    int maxFlow = 0;
    int minCost = 0;

    int src = 0;
    int des = n + m + 1;
    int N = n + m + 2;

    int[][] costDP = new int[N][N];
    int[][] flowDP = new int[N][N];

    // initDP
    initDP(n, m, dp, costDP, flowDP);
    // debug
    System.out.printf("n: %d, m: %d\n", n, m);
    System.out.println("costDP: " + Arrays.deepToString(costDP));
    System.out.println("flowDP: " + Arrays.deepToString(flowDP));

    // for Edmond-karps algo
    boolean[] visited = new boolean[N];
    int[] P = new int[N];

    // Edmond-karps algo
    while (true) {
      int bottleNeck = INF;
      int tempCost = 0;

      Arrays.fill(visited, false);
      Arrays.fill(P, -1);

      LinkedList<Integer> Q = new LinkedList<Integer>();
      Q.add(src);

      while (Q.size() != 0) {
        int curNode = Q.poll();
        System.out.println("curNode: " + curNode);

        visited[curNode] = true;
        if (curNode == des)
          break;

        int preCost = ((curNode == src) ? -1 : costDP[P[curNode]][curNode]);
        for (int nextNode = 0; nextNode < N; nextNode++) {
          if (visited[nextNode] == false) {
            int nextCost = costDP[curNode][nextNode];

            boolean flowable = (flowDP[curNode][nextNode] > 0);
            boolean goodWay =
                (P[curNode] == 0) || (nextNode == des) ||
                (Math.abs(nextCost) * -1 > Math.abs(preCost) * -1);
            if (flowable && goodWay) {
              // go flow
              bottleNeck = Math.min(bottleNeck, flowDP[curNode][nextNode]);
              P[nextNode] = curNode;
              Q.add(nextNode);
            }
          }
        }
      }

      // check found
      if (visited[des] == false)
        break;

      // update
      int t = des;
      System.out.println("P: " + Arrays.toString(P));
      System.out.println("visited: " + Arrays.toString(visited));
      while (P[t] >= 0) {
        // update flow
        flowDP[t][P[t]] += bottleNeck;
        flowDP[P[t]][t] -= bottleNeck;
        tempCost += costDP[P[t]][t];
        t = P[t];
      }
      // update maximum flow and minCost
      maxFlow += bottleNeck;
      minCost += tempCost;
    }
    System.out.println("minCost: " + (minCost * -1));
    return minCost * -1;
  }
  private int findMax(int i, int j) {
    // one of them is leaf
    if (children1[i].size() == 0 || children2[j].size() == 0)
      return 1;

    ArrayList<Integer> curChildren1 = children1[i];
    ArrayList<Integer> curChildren2 = children2[j];

    int n = Math.max(curChildren1.size(), curChildren2.size());
    int m = Math.min(curChildren1.size(), curChildren2.size());

    // min cost flow problem
    // 1. DP 만들기
    int[][] dp = new int[n][m];
    for (int x = 0; x < n; x++) {
      for (int y = 0; y < m; y++) {
        if (curChildren1.size() >= curChildren2.size())
          dp[x][y] = findMax(curChildren1.get(x), curChildren2.get(y)) * -1;
        else
          dp[x][y] = findMax(curChildren1.get(y), curChildren2.get(x)) * -1;
      }
    }

    int ret = MCMF(n, m, dp);
    // System.out.println("ret: " + ret);
    return ret + 1;
  }

  public int solution(int n1, int[][] g1, int n2, int[][] g2) {
    int answer = 0;

    ArrayList<Integer>[] edgeList1 = UserUtills.makeArrOfArrList(n1, g1);
    ArrayList<Integer>[] edgeList2 = UserUtills.makeArrOfArrList(n2, g2);

    children1 = new ArrayList[n1];
    children2 = new ArrayList[n2];
    UserUtills.findChildren(-1, 0, edgeList1, children1);
    UserUtills.findChildren(-1, 0, edgeList2, children2);

    answer = findMax(0, 0);
    return answer;
  }
}

class UserUtills {
  public static void showPQ(PriorityQueue<int[]> pq) {
    for (int[] e : pq) {
      System.out.printf(Arrays.toString(e) + " ,");
    }
    System.out.printf("\n");
  }
  public static ArrayList<Integer>[] makeArrOfArrList(int n, int[][] g) {
    ArrayList<Integer>[] ret = new ArrayList[n];
    // initialize
    for (int i = 0; i < n; i++) {
      ret[i] = new ArrayList<Integer>();
    }
    for (int[] edge : g) {
      int v1 = edge[0] - 1;
      int v2 = edge[1] - 1;
      ret[v1].add(v2);
      ret[v2].add(v1);
    }
    return ret;
  }
  public static void findChildren(int prev, int cur, ArrayList<Integer>[] el,
                                  ArrayList<Integer>[] children) {
    // initialize
    children[cur] = new ArrayList<Integer>();
    for (int v : el[cur]) {
      if (v == prev)
        continue;
      children[cur].add(v);
      findChildren(cur, v, el, children);
    }
  }
}

class ArrayComparator implements Comparator<int[]> {
  public int compare(int[] a, int[] b) { return ((a[0] - b[0] > 0) ? 1 : -1); }
}
