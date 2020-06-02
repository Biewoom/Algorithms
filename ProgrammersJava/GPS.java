import java.util.*;

public class Main {
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
  public void makeEdgeMap(int[][] edge_list,
                          Map<Integer, HashSet<Integer>> edgeMap) {
    for (int i = 0; i < edge_list.length; i++) {
      int v1 = edge_list[i][0];
      int v2 = edge_list[i][1];

      if (edgeMap.get(v1) == null)
        edgeMap.put(v1, new HashSet<Integer>());
      if (edgeMap.get(v2) == null)
        edgeMap.put(v2, new HashSet<Integer>());

      edgeMap.get(v1).add(v2);
      edgeMap.get(v2).add(v1);
    }
  }
  public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
    int limit = k - 2;
    boolean found = false;
    int answer = 0;

    Map<Integer, HashSet<Integer>> edgeMap =
        new Hashtable<Integer, HashSet<Integer>>();
    makeEdgeMap(edge_list, edgeMap);

    System.out.println("Map: " + edgeMap);
    return 1;
  }
}
