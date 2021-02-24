package com.kakao;

import java.util.*;

public class ShoppingJewerly {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String line = sc.nextLine();
    String[] gems = line.substring(2, line.length() - 2).split("\", \"");

    System.out.println(Arrays.toString(new Solution().solution(gems)));
  }
}

class Solution {
  // Search all jewerly at once
  private final int searchSize(String[] gems) {
    int i = 0;
    Set<String> temp = new HashSet<>();
    for (String gem : gems)
      temp.add(gem);

    return temp.size();
  }
  // initialize map
  private final void initializeMap(Map<String, Integer> gemCountMap,
                                   String[] gems) {
    for (String gem : gems) {
      if (!gemCountMap.containsKey(gem))
        gemCountMap.put(gem, 0);
    }
  }
  // Fetch to right
  // add set and add count
  private final void fetchRight(Map<String, Integer> gemCountMap,
                                Set<String> gemCollectSet, String gem) {
    gemCountMap.put(gem, gemCountMap.get(gem) + 1);
    gemCollectSet.add(gem);
  }

  // mock shrink
  private final boolean checkShrinkible(Map<String, Integer> gemCountMap,
                                        String gem) {
    return (gemCountMap.get(gem) >= 2) ? true : false;
  }

  // shrink from left
  private final void shrinkLeft(Map<String, Integer> gemCountMap,
                                Set<String> gemCollectSet, String gem) {
    if (gemCountMap.get(gem) == 1)
      gemCollectSet.remove(gem);

    gemCountMap.put(gem, gemCountMap.get(gem) - 1);
  }

  // checkAndRecord answer
  private final void checkAndRecord(int[] answer, int leftPoint,
                                    int rightPoint) {
    if (answer[0] == 0 && answer[1] == 0) {
      answer[0] = leftPoint;
      answer[1] = rightPoint;
      return;
    }

    if ((rightPoint - leftPoint) < (answer[1] - answer[0])) {
      answer[0] = leftPoint;
      answer[1] = rightPoint;
      return;
    }

    return;
  }

  public int[] solution(String[] gems) {
    int[] answer = new int[2];

    Set<String> gemCollectSet = new HashSet<>();
    Map<String, Integer> gemCountMap = new HashMap<>();

    int maxSize = searchSize(gems);
    initializeMap(gemCountMap, gems);

    int leftPoint = 0, rightPoint = 0;

    while (leftPoint < gems.length) {

      // if gemCollectSet size is lower than maxSize
      while (rightPoint < gems.length && gemCollectSet.size() < maxSize)
        fetchRight(gemCountMap, gemCollectSet, gems[rightPoint++]);

      // make my range be as short as possible
      while (checkShrinkible(gemCountMap, gems[leftPoint]))
        shrinkLeft(gemCountMap, gemCollectSet, gems[leftPoint++]);

      // check and record
      if (gemCollectSet.size() == maxSize)
        checkAndRecord(answer, leftPoint, rightPoint);

      // Just move leftPoint to one step
      shrinkLeft(gemCountMap, gemCollectSet, gems[leftPoint++]);
    }
    answer[0]++;
    return answer;
  }
}
