package com.kakao.test;

import java.util.*;

public class ExploreCave {
  private static final int PATH_X = 8;
  private static final int PATH_Y = 2;
  private static final int ORDER_X = 3;
  private static final int ORDER_Y = 2;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n;
    int[][] path = new int[PATH_X][PATH_Y];
    int[][] order = new int[ORDER_X][ORDER_Y];

    n = Integer.parseInt(sc.nextLine());
    ParsingString.make2DIntArray(sc.nextLine(), path);
    ParsingString.make2DIntArray(sc.nextLine(), order);

    System.out.println(new Solution().solution(n, path, order));
  }
}

class Solution {
  public boolean solution(int n, int[][] path, int[][] order) {

    boolean answer = true;
    return answer;
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
