package com.kakao;

import UserDefined.ParsingString;
import java.util.*;

public class PushKeys {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int index = 0;

    String line = sc.nextLine();
    String[] ll = line.split(",");

    String hands;
    int[] numbers = new int[ll.length];

    for (String l : ll) {
      numbers[index++] = Integer.parseInt(l);
    }
    hands = sc.nextLine();
    System.out.println(new Solution().solution(numbers, hands));
  }
}

class Solution {
  private void makeDistanceArray(int[][] arr) {
    for (int startIndex = 0; startIndex < 12; startIndex++) {
      for (int endIndex = 0; endIndex < 12; endIndex++) {
        int startX, startY;
        int endX, endY;

        startX = startIndex / 3;
        startY = startIndex % 3;

        endX = endIndex / 3;
        endY = endIndex % 3;

        arr[startIndex][endIndex] =
            Math.abs(endX - startX) + Math.abs(endY - startY);
      }
    }
  }
  private int rightMove(StringBuilder builder, int number) {
    builder.append("R");
    return number;
  }
  private int leftMove(StringBuilder builder, int number) {
    builder.append("L");
    return number;
  }

  public String solution(int[] numbers, String hand) {
    int[][] d2Array = new int[12][12];
    makeDistanceArray(d2Array);

    int leftHand = 9;
    int rightHand = 11;
    StringBuilder builder = new StringBuilder();

    for (int number : numbers) {
      number = (numer == 0) ? 10 : --number;

      if (number == 0 || number == 3 || number == 6)
        leftHand = leftMove(builder, number);
      else if (number == 2 || number == 5 || number == 8)
        rightHand = rightMove(builder, number);
      else {
        // when the number is in [1, 4, 7]
        int leftDistance = d2Array[leftHand][number];
        int rightDistance = d2Array[rightHand][number];

        if (leftDistance > rightDistance)
          rightHand = rightMove(builder, number);
        else if (leftDistance < rightDistance)
          leftHand = leftMove(builder, number);
        else {
          // if distances are equlas!
          if (hand.equals("right"))
            rightHand = rightMove(builder, number);
          else
            leftHand = leftMove(builder, number);
        }
      }
    }
    return builder.toString();
  }
}

public class Utils {
  public static void printArray(int[] arr) {
    for (int a : arr) {
      System.out.println(a);
    }
  }
}
