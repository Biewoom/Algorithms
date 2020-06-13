import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String line = sc.nextLine();
    String[] lines = line.substring(1, line.length() - 1).split("\\],\\[");

    int i = 0;
    int[][] rectangles = new int[lines.length][4];

    for (String ll : lines) {
      String[] temp = ll.split(", ");
      int j = 0;
      for (String s : temp) {
        rectangles[i][j] = Integer.parseInt(s);
        j++;
      }
      i++;
    }
    System.out.println(new Solution().solution(rectangles));
    sc.close();
  }
}

class Solution {

  private void compressionCoord(int[][] rectangles,
                                Map<Integer, Integer> xIndexMap,
                                Map<Integer, Integer> yIndexMap) {
    HashSet<Integer> xSet = new HashSet<Integer>();
    HashSet<Integer> ySet = new HashSet<Integer>();

    for (int[] rectangle : rectangles) {
      int x1 = rectangle[0];
      int y1 = rectangle[1];

      int x2 = rectangle[2];
      int y2 = rectangle[3];

      xSet.add(x1);
      xSet.add(x2);
      ySet.add(y1);
      ySet.add(y2);
    }

    List<Integer> xList = new ArrayList<>(xSet);
    List<Integer> yList = new ArrayList<>(ySet);

    Collections.sort(xList);
    Collections.sort(yList);

    for (int i = 0; i < xList.size(); i++) {
      xIndexMap.put(xList.get(i), i);
    }
    for (int i = 0; i < yList.size(); i++) {
      yIndexMap.put(yList.get(i), i);
    }
    return;
  }

  private void setDistanceRecord(Map<Integer, Integer> indexMap,
                                 Map<Integer, Integer> distanceMap) {

    Map<Integer, Integer> temp = new Hashtable<Integer, Integer>();
    for (Integer key : indexMap.keySet()) {
      temp.put(indexMap.get(key), key);
    }

    int i = 0;
    while (temp.get(i + 1) != null) {
      distanceMap.put(i, temp.get(i + 1) - temp.get(i));
      i++;
    }
    return;
  }

  private void mapAdd(Map<Integer, Integer> map, int a) {
    if (map.get(a) == null)
      map.put(a, 1);
    else
      map.put(a, map.get(a) + 1);
  }
  private void mapSubtract(Map<Integer, Integer> map, int a) {
    if (map.get(a) == null)
      map.put(a, -1);
    else
      map.put(a, map.get(a) - 1);
  }

  private void mapsInit(int[][] rectangles, Map<Integer, Integer> xIndexMap,
                        Map<Integer, Integer> yIndexMap,
                        Map<Integer, Hashtable<Integer, Integer>> cntMap) {
    // initialize
    List<Integer> xIndexes = new ArrayList<Integer>(xIndexMap.values());

    for (int xIndex : xIndexes) {
      cntMap.put(xIndex, new Hashtable<Integer, Integer>());
    }

    for (int[] rectangle : rectangles) {
      int indexOfStartX = xIndexMap.get(rectangle[0]);
      int indexOfEndX = xIndexMap.get(rectangle[2]);

      int indexOfY1 = yIndexMap.get(rectangle[1]);
      int indexOfY2 = yIndexMap.get(rectangle[3]);

      Map<Integer, Integer> m1 = cntMap.get(indexOfStartX);
      Map<Integer, Integer> m2 = cntMap.get(indexOfEndX);

      for (int y = indexOfY1; y < indexOfY2; y++) {
        mapAdd(m1, y);
        mapSubtract(m2, y);
      }
    }
  }

  private long calculateArea(List<Integer> Xs,
                             Map<Integer, Hashtable<Integer, Integer>> cntMap,
                             Map<Integer, Integer> xDistanceMap,
                             Map<Integer, Integer> yDistanceMap) {
    // fenwick tree
    long result = 0;
    int ysSize = yDistanceMap.keySet().size();

    int[] colored = new int[ysSize];
    long[] fenwickTree = new long[ysSize + 1];

    for (int x : Xs) {
      if (x != 0)
        result += (long)xDistanceMap.get(x - 1) * FenwickUtil.sum(fenwickTree);
      // update add
      for (Map.Entry<Integer, Integer> E : cntMap.get(x).entrySet()) {
        int y = E.getKey();
        int cnt = E.getValue();
        if (cnt == 0)
          continue;
        else if (colored[y] == 0 && cnt > 0)
          FenwickUtil.add(fenwickTree, y + 1, yDistanceMap.get(y));
        else if ((colored[y] + cnt) == 0)
          FenwickUtil.subtract(fenwickTree, y + 1, yDistanceMap.get(y));
        colored[y] += cnt;
      }
    }
    return result;
  }
  public long solution(int[][] rectangles) {
    long answer;
    // 1. 좌표압축
    Map<Integer, Integer> xIndexMap = new Hashtable<Integer, Integer>();
    Map<Integer, Integer> yIndexMap = new Hashtable<Integer, Integer>();
    compressionCoord(rectangles, xIndexMap, yIndexMap);

    // 2. 거리 기록
    Map<Integer, Integer> xDistanceMap = new Hashtable<Integer, Integer>();
    Map<Integer, Integer> yDistanceMap = new Hashtable<Integer, Integer>();
    setDistanceRecord(xIndexMap, xDistanceMap);
    setDistanceRecord(yIndexMap, yDistanceMap);
    // 3. Plane Sweeping 하기
    Map<Integer, Hashtable<Integer, Integer>> cntMap =
        new Hashtable<Integer, Hashtable<Integer, Integer>>();
    mapsInit(rectangles, xIndexMap, yIndexMap, cntMap);
    // 4. x 기준으로 input 순서 만들기
    List<Integer> xInputs = new ArrayList<Integer>(xIndexMap.values());
    Collections.sort(xInputs);
    // 5. Fenwick 트리 이용한 넓이 합 구하기.
    answer = calculateArea(xInputs, cntMap, xDistanceMap, yDistanceMap);

    return answer;
  }
}

final class FenwickUtil {
  private FenwickUtil() {}
  public static void add(long[] fenwickTree, int index, int value) {
    int n = fenwickTree.length;
    for (; index < n; index += (index & -index)) {
      fenwickTree[index] += value;
    }
  }
  public static void subtract(long[] fenwickTree, int index, int value) {
    int n = fenwickTree.length;
    for (; index < n; index += (index & -index)) {
      fenwickTree[index] -= value;
    }
  }

  public static long sum(long[] fenwickTree) {
    long ret = 0;
    int i = fenwickTree.length - 1;
    while (i > 0) {
      ret += fenwickTree[i];
      i -= (i & -i);
    }
    return ret;
  }
}
