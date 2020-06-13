import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int m = Integer.parseInt(sc.nextLine());
    int n = Integer.parseInt(sc.nextLine());

    String[] board = new String[m];
    String[] lines = sc.nextLine().split(", ");

    for (int i = 0; i < m; i++) {
      String input = lines[i].substring(1, n + 1);
      board[i] = input;
    }
    String result = new Solution().solution(m, n, board);
    System.out.println(result);
  }
}

class Solution {

  public int checkRemovability(int m, int n, char[][] charBoard) {
    char finalRemover = 'a';

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        // <First> I'm a wall, Skip myself!
        if (charBoard[i][j] == '*')
          continue;
        // <Second> I'm a point which help some tile to find his partener!
        else if (charBoard[i][j] == '.') {
          // there are four cases:
          char upperCh = userFind.findUpper(m, n, i - 1, j, charBoard);
          char lowerCh = userFind.findLower(m, n, i + 1, j, charBoard);
          char leftCh = userFind.findLeft(m, n, i, j - 1, charBoard);
          char rightCh = userFind.findRight(m, n, i, j + 1, charBoard);
          // 1: upper meet left
          if (upperCh != '*' && upperCh != '.' && upperCh == leftCh)
            finalRemover = userFind.findMin(finalRemover, upperCh);
          // 2: upper meet right
          if (upperCh != '*' && upperCh != '.' && upperCh == rightCh)
            finalRemover = userFind.findMin(finalRemover, upperCh);
          // 3: lower meet left
          if (lowerCh != '*' && lowerCh != '.' && lowerCh == leftCh)
            finalRemover = userFind.findMin(finalRemover, lowerCh);
          // 4: lower meet right
          if (lowerCh != '*' && lowerCh != '.' && lowerCh == rightCh)
            finalRemover = userFind.findMin(finalRemover, lowerCh);
        }
        // <Third> I'm a tile and find my partener!
        else {
          char curCh = charBoard[i][j];
          if (curCh == userFind.findRight(m, n, i, j + 1, charBoard))
            finalRemover = userFind.findMin(finalRemover, curCh);
          if (curCh == userFind.findLower(m, n, i + 1, j, charBoard))
            finalRemover = userFind.findMin(finalRemover, curCh);
        }
      }
    }
    return ((finalRemover == 'a') ? -1 : (int)finalRemover);
  }
  public void Remove(int m, int n, char[][] charBoard, char ch) {
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (charBoard[i][j] == ch)
          charBoard[i][j] = '.';
      }
    }
  }

  public void backTracking(int leftTiles, int m, int n, char[][] charBoard,
                           ArrayList<Character> answerList) {
    if (leftTiles <= 0)
      return;

    int toBeRemovedTile = checkRemovability(m, n, charBoard);
    for (int i = 0; i < m; i++)
      System.out.println(Arrays.toString(charBoard[i]));
    if (toBeRemovedTile > 0) {
      Remove(m, n, charBoard, (char)toBeRemovedTile);
      answerList.add((char)toBeRemovedTile);
      backTracking(leftTiles - 1, m, n, charBoard, answerList);
    } else
      return;
  }

  public String solution(int m, int n, String[] board) {

    char[][] charBoard = new char[m][n];
    ArrayList<Character> answerList = new ArrayList<Character>();

    userUtil.initializeCharBoard(m, n, charBoard, board);
    int tilesNumber = userUtil.checkTiles(m, n, charBoard);

    backTracking(tilesNumber, m, n, charBoard, answerList);
    return ((answerList.size() == tilesNumber) ? userUtil.getString(answerList)
                                               : "IMPOSSIBLE");
  }
}

class userFind {
  public static char findRight(int m, int n, int x, int y, char[][] charBoard) {
    while (y < n && charBoard[x][y] == '.') {
      y++;
    }
    return ((y >= n) ? '*' : charBoard[x][y]);
  }
  public static char findLeft(int m, int n, int x, int y, char[][] charBoard) {
    while (y > 0 && charBoard[x][y] == '.') {
      y--;
    }
    return ((y < 0) ? '*' : charBoard[x][y]);
  }
  public static char findUpper(int m, int n, int x, int y, char[][] charBoard) {
    while (x > 0 && charBoard[x][y] == '.') {
      x--;
    }
    return ((x < 0) ? '*' : charBoard[x][y]);
  }
  public static char findLower(int m, int n, int x, int y, char[][] charBoard) {
    while (x < m && charBoard[x][y] == '.') {
      x++;
    }
    return ((x >= m) ? '*' : charBoard[x][y]);
  }
  public static char findMin(char a, char b) {
    if (a <= b)
      return a;
    else
      return b;
  }
}

class userUtil {
  public static String getString(ArrayList<Character> list) {
    StringBuilder builder = new StringBuilder(list.size());
    for (char ch : list) {
      builder.append(ch);
    }
    return builder.toString();
  }
  public static void initializeCharBoard(int m, int n, char[][] charBoard,
                                         String[] board) {
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        charBoard[i][j] = board[i].charAt(j);
      }
    }
  }
  public static int checkTiles(int m, int n, char[][] charBoard) {
    HashSet<Character> tempSet = new HashSet<Character>();
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (charBoard[i][j] != '.' && charBoard[i][j] != '*')
          tempSet.add(charBoard[i][j]);
      }
    }
    return tempSet.size();
  }
}
