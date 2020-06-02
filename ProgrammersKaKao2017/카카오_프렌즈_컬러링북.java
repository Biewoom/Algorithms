import java.util.*;

class Solution {

  public static int Find(int index, int[] P) {
    if (P[index] == -1)
      return index;
    else
      return Find(P[index], P);
  }

  public static void Union_Find(int index1, int index2, int[] P, int[] Size) {
    int x = Find(index1, P);
    int y = Find(index2, P);

    if (x != y) {
      if (Size[x] >= Size[y]) {
        P[y] = x;
        Size[x] += Size[y];
      } else {
        P[x] = y;
        Size[y] += Size[x];
      }
    }
  }

  public static int[] solution(int m, int n, int[][] picture) {
    int numberOfArea = 0;
    int maxSizeOfOneArea = 0;

    int[] P = new int[m * n];
    int[] Size = new int[m * n];
    Arrays.fill(P, -2);

    int index, indexLocatedRight, indexLocatedLower;
    // initialize //
    for (int row = 0; row < m; row++) {
      for (int col = 0; col < n; col++) {
        index = row * n + col;
        if (picture[row][col] != 0) {
          P[index] = -1;
          Size[index] = 1;
        }
      }
    }

    for (int row = 0; row < m; row++) {
      for (int col = 0; col < n; col++) {
        index = row * n + col;
        if (col != n - 1) {
          indexLocatedRight = index + 1;
          if (picture[row][col] != 0 &&
              picture[row][col] == picture[row][col + 1])
            Union_Find(index, indexLocatedRight, P, Size);
        }
        if (row != m - 1) {
          indexLocatedLower = index + n;
          if (picture[row][col] != 0 &&
              picture[row][col] == picture[row + 1][col])
            Union_Find(index, indexLocatedLower, P, Size);
        }
      }
    }

    for (int areaElem : P) {
      if (areaElem == -1)
        numberOfArea++;
    }
    for (int sizeElem : Size) {
      if (maxSizeOfOneArea < sizeElem)
        maxSizeOfOneArea = sizeElem;
    }

    int[] answer = new int[2];
    answer[0] = numberOfArea;
    answer[1] = maxSizeOfOneArea;
    return answer;
  }

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int m = Integer.parseInt(scan.nextLine());
    int n = Integer.parseInt(scan.nextLine());
    int[][] picture = new int[m][n];

    String line = scan.nextLine();
    String[] lines = line.substring(2, line.length() - 2).split("\\],\\[");

    int r = 0;
    for (String tempStr : lines) {
      int c = 0;
      String[] tempL = tempStr.split(", ");
      for (String temp : tempL) {
        picture[r][c++] = Integer.parseInt(temp);
      }
      r++;
    }
    scan.close();
    System.out.println(Arrays.toString(solution(m, n, picture)));
  }
}
