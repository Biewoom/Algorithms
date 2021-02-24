import java.io.*;
class Main {
  public static void main(String[] args) throws Exception {
    String A = "apple";
    String B = "apple";
    String C = new String("apple");

    System.out.println("result < A == B > : " + (A == B));
    System.out.println("result < A == C > : " + (A == C));
    System.out.println("result < A.equals(B): " + (A.equals(B)));
    System.out.println("result < A.equals(C): " + (A.equals(C)));

    // Case 1
    for (int i = 0; i < 10; i++) {
      A += "aa";
    }
    // 예상 결과값: A => appleaaaaaaaaaaaaaaaaaaaa

    // Case 2
    StringBuilder sb = new StringBuilder();
    sb.append(A);
    for (int i = 0; i < 10; i++) {
      sb.append("aa");
    }
    A = sb.toString();
    // 예상 결과값: A = appleaaaaaaaaaaaaaaaaaaaa

    System.out.println("after replacing  A: " + A);
    System.out.println("after replacing  B: " + B);
    System.out.println("after replacing  C: " + C);
  }
}
