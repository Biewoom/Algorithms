import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    int[][] data = {{0, 0}, {1, 1}, {0, 2}, {2, 0}};

    System.out.println(new Solution().solution(n, data));
  }
}

class Solution {

  boolean checkValid(int[] leftMostCoord, int[] rightMostCoord, int[][] sumDP) {

    int x1 = leftMostCoord[0] + 1;
    int y1 = leftMostCoord[1] + 1;

    int x2 = rightMostCoord[0] - 1;
    int y2 = rightMostCoord[1] - 1;

    int Area;
    if (x1 > x2 || y1 > y2)
      Area = 0;
    else
      Area = sumDP[x2][y2] - sumDP[x2][y1 - 1] - sumDP[x1 - 1][y2] +
             sumDP[x1 - 1][y1 - 1];

    if (Area == 0)
      return true;
    else
      return false;
  }

  void sumArray(int m, int n, int[][] sumDP) {
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i == 0 && j == 0)
          continue;
        else if (i == 0)
          sumDP[i][j] += sumDP[i][j - 1];
        else if (j == 0)
          sumDP[i][j] += sumDP[i - 1][j];
        else
          sumDP[i][j] +=
              sumDP[i - 1][j] + sumDP[i][j - 1] - sumDP[i - 1][j - 1];
      }
    }
  }

  public int solution(int n, int[][] data) {

    int answer = 0;

    HashSet<Integer> xHashSet = new HashSet<Integer>();
    HashSet<Integer> yHashSet = new HashSet<Integer>();

    for (int[] d : data) {
      int x = d[0];
      int y = d[1];
      xHashSet.add(x);
      yHashSet.add(y);
    }

    List<Integer> xList = new ArrayList<>(xHashSet);
    List<Integer> yList = new ArrayList<>(yHashSet);
    Collections.sort(xList);
    Collections.sort(yList);

    int Xacc = 0;
    int Yacc = 0;
    Map<Integer, Integer> xHashMap = new Hashtable<Integer, Integer>();
    Map<Integer, Integer> yHashMap = new Hashtable<Integer, Integer>();

    for (int x : xList) {

      if (xHashMap.get(x) == null) {
        xHashMap.put(x, Xacc);
        Xacc++;
      }
    }

    for (int y : yList) {
      if (yHashMap.get(y) == null) {
        yHashMap.put(y, Yacc);
        Yacc++;
      }
    }

    int[][] sumDP = new int[Xacc][Yacc];
    for (int[] d : data) {
      int x = d[0];
      int y = d[1];
      sumDP[xHashMap.get(x)][yHashMap.get(y)] = 1;
    }

    sumArray(Xacc, Yacc, sumDP);

    for (int i = 0; i < data.length; i++) {
      for (int j = i + 1; j < data.length; j++) {
        int x1 = data[i][0];
        int y1 = data[i][1];

        int x2 = data[j][0];
        int y2 = data[j][1];

        if (x1 == x2 || y1 == y2)
          continue;
        else {
          int xIndex1 = xHashMap.get(x1);
          int xIndex2 = xHashMap.get(x2);

          int yIndex1 = yHashMap.get(y1);
          int yIndex2 = yHashMap.get(y2);

          int[] rightMostCoord = {Math.max(xIndex1, xIndex2),
                                  Math.max(yIndex1, yIndex2)};
          int[] leftMostCoord = {Math.min(xIndex1, xIndex2),
                                 Math.min(yIndex1, yIndex2)};

          boolean check = checkValid(leftMostCoord, rightMostCoord, sumDP);
          if (check)
            answer++;
        }
      }
    }
    return answer;
  }
}
