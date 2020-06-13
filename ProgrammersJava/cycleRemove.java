import java.util.*;

public class cycleRemove {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = Integer.parseInt(sc.nextLine());
    String line = sc.nextLine();
    String[] lines = line.substring(1, line.length() - 1).split("\\],\\[");

    int[][] edges = new int[lines.length][2];

    for (int i = 0; i < lines.length; i++) {
      String[] ll = lines[i].split(",");
      edges[i][0] = Integer.parseInt(ll[0]);
      edges[i][1] = Integer.parseInt(ll[1]);
    }
    System.out.println(new Solution().solution(n, edges));
  }
}

class Solution {
  static int index = 0;
  int[] desnums;
  int[] edgenums;
  ArrayList<Integer>[] edgeList;

  public void edgeListInit(int n, int[][] edges,
                           ArrayList<Integer>[] edgeList) {

    HashSet<Integer>[] tempHashset = new HashSet[n];
    for (int i = 0; i < n; i++) {
      tempHashset[i] = new HashSet<Integer>();
    }

    for (int[] edge : edges) {
      int v1 = edge[0] - 1;
      int v2 = edge[1] - 1;

      tempHashset[v1].add(v2);
      tempHashset[v2].add(v1);
    }

    for (int i = 0; i < n; i++) {
      edgeList[i] = new ArrayList<Integer>(tempHashset[i]);
    }
  }
  public void edgenumsInit(int n, int[] edgenums) {
    for (int i = 0; i < n; i++) {
      edgenums[i] = edgeList[i].size();
    }
  }
  public void desnumsInit(int n, int[] desnums) {
    HashSet<Integer> visited = new HashSet<Integer>();
    int[] dfsn = new int[n];
    dfs(-1, 0, dfsn, visited);
  }
  public int dfs(int prev, int cur, int[] dfsn, HashSet<Integer> visited) {

    int ret = dfsn[cur] = index++;
    int tmp;
    visited.add(cur);

    for (int nxt : edgeList[cur]) {
      if (!visited.contains(nxt))
        tmp = dfs(cur, nxt, dfsn, visited);
      else {
        tmp = dfsn[nxt];
        if (tmp > dfsn[cur])
          continue;
      }
      if (tmp >= dfsn[cur])
        desnums[cur]++;

      ret = Math.min(ret, tmp);
    }
    if (prev == -1)
      desnums[cur] = Math.max(0, desnums[cur] - 1);
    return ret;
  }
  public int calculateTotalEdges(int n, int[] edgenums) {
    int result = 0;
    for (int i = 0; i < n; i++) {
      result += edgenums[i];
    }
    result /= 2;
    return result;
  }

  public int solution(int n, int[][] edges) {
    int answer = 0;
    int totalEdges = 0;
    edgeList = new ArrayList[n];
    edgenums = new int[n];
    desnums = new int[n];

    edgeListInit(n, edges, edgeList);
    edgenumsInit(n, edgenums);
    desnumsInit(n, desnums);

    totalEdges = calculateTotalEdges(n, edgenums);
    for (int i = 0; i < n; i++) {
      if ((totalEdges - edgenums[i] + desnums[i]) < (n - 1))
        answer += i + 1;
    }
    return answer;
  }
}
