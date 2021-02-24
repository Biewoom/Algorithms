package AreaOfRectangles;
import java.util.*;

public class main {
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

  public void mapAdd(Map<Integer, ArrayList<ArrayList<Integer>>> Map, int a,
                     ArrayList<Integer> arr) {
    if (Map.get(a) == null)
      Map.put(a, new ArrayList<ArrayList<Integer>>());
    Map.get(a).add(arr);
  }
  public void
  setInputMap(int[][] rectangles, Map<Integer, Integer> xIndexMap,
              Map<Integer, ArrayList<ArrayList<Integer>>> inputMap) {
    for (int[] rectangle : rectangles) {
      int x1 = xIndexMap.get(rectangle[0]);
      int x2 = xIndexMap.get(rectangle[2]);

      int y1 = rectangle[1];
      int y2 = rectangle[3];

      ArrayList<Integer> temp = new ArrayList<Integer>();
      temp.add(x2);
      temp.add(y1);
      temp.add(y2);

      mapAdd(inputMap, x1, temp);
    }
  }
  public long calculateArea(PriorityQueue<ArrayList<Integer>> pq) {

    // extract
    List<ArrayList<Integer>> sortedArr = new ArrayList<ArrayList<Integer>>();
    for (ArrayList<Integer> arr : pq) {
      sortedArr.add(new ArrayList<Integer>(arr.subList(1, arr.size())));
    }
    Collections.sort(sortedArr, new ArrayListComparator());

    if (sortedArr.size() == 0)
      return 0;

    long ret = 0;
    int leftMostY = sortedArr.get(0).get(0);
    int rightMostY = sortedArr.get(0).get(1);

    for (int i = 1; i < sortedArr.size(); i++) {
      int newLeftY = sortedArr.get(i).get(0);
      int newRightY = sortedArr.get(i).get(1);

      if (newLeftY <= rightMostY)
        rightMostY = Math.max(rightMostY, newRightY);
      else {
        ret += (long)(rightMostY - leftMostY);
        leftMostY = newLeftY;
        rightMostY = newRightY;
      }
    }
    ret += (long)(rightMostY - leftMostY);
    return ret;
  }
  public long solution(int[][] rectangles) {
    long answer = 0;
    // 1.좌표압축
    Map<Integer, Integer> xIndexMap = new Hashtable<Integer, Integer>();
    CoordSet.setIndexMaps(rectangles, xIndexMap);
    // debug
    // System.out.println("xIndexMap: " + xIndexMap);

    // 2.거리 측정
    Map<Integer, Integer> xDistanceMap = new Hashtable<Integer, Integer>();
    CoordSet.setDistanceMap(xIndexMap, xDistanceMap);
    // debug
    // System.out.println("xDistanceMap: " + xDistanceMap);

    // 3. InputMap
    Map<Integer, ArrayList<ArrayList<Integer>>> inputMap =
        new Hashtable<Integer, ArrayList<ArrayList<Integer>>>();
    setInputMap(rectangles, xIndexMap, inputMap);

    // 5. plane sweeping(heap 이용해서)
    PriorityQueue<ArrayList<Integer>> pq =
        new PriorityQueue<ArrayList<Integer>>(rectangles.length,
                                              new ArrayListComparator());

    // 6. Xflows
    ArrayList<Integer> xFlows = new ArrayList<Integer>(xIndexMap.values());
    Collections.sort(xFlows);

    for (int x : xFlows) {
      // 넓이 구하기
      if (x != 0)
        answer += (long)xDistanceMap.get(x - 1) * calculateArea(pq);
      // 들어 갈거 드가기
      ArrayList<ArrayList<Integer>> mapE = inputMap.get(x);
      if (mapE != null) {
        for (ArrayList<Integer> E : mapE) {
          pq.add(E);
        }
      }
      // 빠질거 빠지기
      while ((pq.size() != 0) && (pq.peek().get(0) <= x)) {
        pq.poll();
      }
      // System.out.println("x: " + x);
      // System.out.println("answer: " + answer);
      // System.out.println("pq: " + pq);
    }
    return answer;
  }
}

class CoordSet {
  public static void setIndexMaps(int[][] rectangles,
                                  Map<Integer, Integer> xIndexMap) {
    Set<Integer> hashX = new HashSet<Integer>();

    for (int[] rectangle : rectangles) {
      int x1 = rectangle[0];
      int x2 = rectangle[2];

      hashX.add(x1);
      hashX.add(x2);
    }

    List<Integer> xList = new ArrayList<Integer>(hashX);

    Collections.sort(xList);

    int xAcc = 0;
    for (int x : xList) {
      xIndexMap.put(x, xAcc++);
    }
  }

  public static void setDistanceMap(Map<Integer, Integer> indexMap,
                                    Map<Integer, Integer> distanceMap) {

    Map<Integer, Integer> reverseMap = new Hashtable<Integer, Integer>();

    for (Map.Entry<Integer, Integer> E : indexMap.entrySet()) {
      reverseMap.put(E.getValue(), E.getKey());
    }
    int indexes = indexMap.size() - 1;
    for (int i = 0; i < indexes; i++) {
      distanceMap.put(i, reverseMap.get(i + 1) - reverseMap.get(i));
    }
  }
}

class ArrayListComparator implements Comparator<ArrayList<Integer>> {
  public int compare(ArrayList<Integer> arr1, ArrayList<Integer> arr2) {
    if (arr1.size() == 0)
      return 0;
    else if (arr1.get(0) == arr2.get(0))
      return compare(new ArrayList<Integer>(arr1.subList(1, arr1.size())),
                     new ArrayList<Integer>(arr2.subList(1, arr2.size())));
    else if (arr1.get(0) > arr2.get(0))
      return 1;
    else
      return -1;
  }
}
