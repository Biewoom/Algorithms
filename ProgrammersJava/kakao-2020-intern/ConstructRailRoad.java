package com.kakao.test;

import java.util.*;

public class ConstructRailRoad {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int[][] board = new int[4][4];
    ParsingString.make2DIntArray(sc.nextLine(), board);

    System.out.println(new Solution().solution(board));
  }
}

class Solution {
  private int[][][] dp;
  private int[][] boardRef;

  private boolean isRightMovable(int pose, int x, int y) {
    if ((y + 1) >= boardRef[0].length)
      return false;

    if (boardRef[x][y + 1] == 1)
      return false;

    int nextCost = (pose == 1) ? dp[pose][x][y] + 100 : dp[pose][x][y] + 600;

    if (nextCost >= dp[1][x][y + 1])
      return false;

    dp[1][x][y + 1] = nextCost;
    return true;
  }

  private boolean isLeftMovable(int pose, int x, int y) {
    if ((y - 1) < 0)
      return false;

    if (boardRef[x][y - 1] == 1)
      return false;

    int nextCost = (pose == 1) ? dp[pose][x][y] + 100 : dp[pose][x][y] + 600;

    if (nextCost >= dp[1][x][y - 1])
      return false;

    dp[1][x][y - 1] = nextCost;
    return true;
  }
  private boolean isUpperMovable(int pose, int x, int y) {
    if ((x - 1) < 0)
      return false;

    if (boardRef[x - 1][y] == 1)
      return false;

    int nextCost = (pose == 0) ? dp[pose][x][y] + 100 : dp[pose][x][y] + 600;

    if (nextCost >= dp[0][x - 1][y])
      return false;

    dp[0][x - 1][y] = nextCost;
    return true;
  }
  private boolean isLowerMovable(int pose, int x, int y) {
    if ((x + 1) >= boardRef.length)
      return false;

    if (boardRef[x + 1][y] == 1)
      return false;

    int nextCost = (pose == 0) ? dp[pose][x][y] + 100 : dp[pose][x][y] + 600;

    if (nextCost >= dp[0][x + 1][y])
      return false;

    dp[0][x + 1][y] = nextCost;
    return true;
  }

  public int solution(int[][] board) {
    int n = board.length;
    int m = board[0].length;

    int answer = 0;
    // 0 = veritcal, 1 = horizontal
    dp = new int[2][n][m];
    boardRef = board;

    Util.fillMax(dp);
    // hard coding
    dp[0][0][0] = 0;
    dp[1][0][0] = 0;
    dp[1][0][1] = 100;
    dp[0][1][0] = 100;

    Queue<int[]> QQ = new LinkedList<>();
    QQ.add(new int[] {1, 0, 1});
    QQ.add(new int[] {0, 1, 0});

    while (QQ.size() > 0) {
      int[] current = QQ.poll();

      // decomposition
      int pose = current[0];
      int x = current[1];
      int y = current[2];

      // if current is box
      if (board[x][y] == 1)
        continue;

      // move rightside
      if (isRightMovable(pose, x, y))
        QQ.add(new int[] {1, x, y + 1});
      // move leftside
      if (isLeftMovable(pose, x, y))
        QQ.add(new int[] {1, x, y - 1});
      // move upperside
      if (isUpperMovable(pose, x, y))
        QQ.add(new int[] {0, x - 1, y});
      // move downside
      if (isLowerMovable(pose, x, y))
        QQ.add(new int[] {0, x + 1, y});
    }
    return Math.min(dp[0][n - 1][m - 1], dp[1][n - 1][m - 1]);
  }
}

public class Util {
  private static final int MAX = Integer.MAX_VALUE;

  public static void fillMax(int[][][] arr) {
    for (int x = 0; x < arr.length; x++) {
      for (int y = 0; y < arr[0].length; y++) {
        for (int z = 0; z < arr[0][0].length; z++) {
          arr[x][y][z] = MAX;
        }
      }
    }
  }
}

public class ParsingString {
  public static void make2DIntArray(String Line, int[][] arr) {
    int m = arr.length;
    int n = arr[0].length;

    String[] ll = Line.substring(1, Line.length() - 1).split("\\],\\[");
    for (int i = 0; i < m; i++) {
      String[] lll = ll[i].split(",");
      for (int j = 0; j < n; j++) {
        arr[i][j] = Integer.parseInt(lll[j]);
      }
    }
  }
}
