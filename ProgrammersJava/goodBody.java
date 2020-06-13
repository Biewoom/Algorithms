import java.util.*;

public class goodBody {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = Integer.parseInt(sc.nextLine());
    int m = Integer.parseInt(sc.nextLine());
    String input = sc.nextLine();
    String[] lines = input.substring(1, input.length() - 1).split("\\],\\[");

    int[][] timetable = new int[m][2];

    for (int i = 0; i < m; i++) {
      String[] ll = lines[i].split(",");
      timetable[i][0] = Integer.parseInt(ll[0]);
      timetable[i][1] = Integer.parseInt(ll[1]);
    }
    System.out.println(new Solution().solution(n, m, timetable));
    sc.close();
  }
}

class Solution {

  static final int INF = 1000 * 1000 + 1;

  int findDistance(int x, int y, ArrayList<int[]> StarArr) {

    int minimum = INF;
    for (int[] Star : StarArr) {
      int _x = Star[0];
      int _y = Star[1];

      int distance = Math.abs(x - _x) + Math.abs(y - _y);
      minimum = Math.min(minimum, distance);
    }
    return minimum;
  }

  int recur(int curIndex, int n, int std, ArrayList<int[]> StartArr) {

    if (curIndex >= n * n)
      return 0;

    int x = curIndex / n;
    int y = curIndex % n;

    int curDistance = findDistance(x, y, StartArr);

    if (curDistance == std) {
      int[] temp = {x, y};
      StartArr.add(temp);
      return 1 + recur(curIndex + 1, n, std, StartArr);
    } else
      return recur(curIndex + 1, n, std, StartArr);
  }

  int findMinimum(int n, int maxPeople) {

    int result = 1;
    int maxDistance = 2 * (n - 1);
    int preBound = 0;
    int curBound = 0;

    // System.out.printf("n: %d, maxPeople: %d\n", n, maxPeople);
    for (int d = maxDistance; d > 0; d--) {
      if (d == 1)
        curBound = n * n;
      else if (d == 2)
        curBound = (n * n) / 2 + (n * n) % 2;
      else {
        int capacity = 0;
        for (int index = 0; index < n; index++) {
          ArrayList<int[]> Arr = new ArrayList<int[]>();
          int[] temp = {0, index};
          Arr.add(temp);
          capacity = Math.max(capacity, 1 + recur(index, n, d, Arr));
        }
        curBound = capacity;
      }

      // boundChecking
      if (maxPeople <= curBound) {
        result = d;
        break;
      }
    }
    return result;
  }

  public int solution(int n, int m, int[][] timetable) {

    Arrays.sort(timetable, new Comparator<int[]>() {
      public int compare(int[] a, int[] b) {
        return ((a[0] == b[0]) ? a[1] - b[1] : a[0] - b[0]);
      }
    });

    PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
    int maxPeople = 0;

    for (int[] time : timetable) {
      int timeStart = time[0];
      int timeEnd = time[1];

      while (pq.size() != 0 && pq.peek() < timeStart) {
        pq.poll();
      }
      pq.add(timeEnd);
      maxPeople = Math.max(maxPeople, pq.size());
    }

    if (maxPeople == 1)
      return 0;
    else
      return findMinimum(n, maxPeople);
  }
}
