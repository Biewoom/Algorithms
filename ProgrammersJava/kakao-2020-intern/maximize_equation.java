package com.kakao;

import java.util.*;

public class Maximize_equation {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String line = sc.nextLine();
    System.out.println(new Solution().solution(line));
  }
}

class Solution {
  private List<char[]> makeOperatorsList() {
    /* 6가지 밖에 안되서 Hard Coding */
    List<char[]> res = new ArrayList<char[]>();
    res.add(new char[] {'+', '-', '*'});
    res.add(new char[] {'+', '*', '-'});
    res.add(new char[] {'*', '+', '-'});
    res.add(new char[] {'*', '-', '+'});
    res.add(new char[] {'-', '+', '*'});
    res.add(new char[] {'-', '*', '+'});
    return res;
  }
  private long operatorExecute(List<Long> ll, char op) {
    if (ll.size() == 1)
      return ll.get(0);

    if (op == '*')
      return operatorExecute(ll.subList(0, ll.size() - 1), op) *
          ll.get(ll.size() - 1);
    else if (op == '-')
      return operatorExecute(ll.subList(0, ll.size() - 1), op) -
          ll.get(ll.size() - 1);
    else
      return operatorExecute(ll.subList(0, ll.size() - 1), op) +
          ll.get(ll.size() - 1);
  }

  private long calculateRecursive(int index, char[] combination,
                                  String expression) {
    if (index < 0)
      return Long.parseLong(expression);

    char currentOp = combination[index];
    int lastEdit = 0;
    List<Long> listOfOperand = new ArrayList<Long>();

    for (int i = 0; i < expression.length(); i++) {
      if (expression.charAt(i) == currentOp) {
        listOfOperand.add(calculateRecursive(
            index - 1, combination, expression.substring(lastEdit, i)));
        lastEdit = i + 1;
      }
    }
    listOfOperand.add(calculateRecursive(index - 1, combination,
                                         expression.substring(lastEdit)));

    return operatorExecute(listOfOperand, currentOp);
  }
  public long solution(String expression) {
    List<char[]> operatorCombinationList = makeOperatorsList();
    long answer = 0;

    for (char[] combination : operatorCombinationList) {
      long value = Math.abs(calculateRecursive(2, combination, expression));
      answer = Math.max(answer, value);
    }

    return answer;
  }
}
