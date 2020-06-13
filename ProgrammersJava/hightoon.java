import java.util.*;

public class hightoon {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    System.out.println(new Solution().solution(n));
  }
}

class Solution {

  int recur(int n, int numberOfPlus) {
    if (n < 1 || 2 * Math.log(n) / Math.log(3) < numberOfPlus) {
      return 0;
    } else if (n == 3 && numberOfPlus == 2) {
      return 1;
    } else if (n == 3 && numberOfPlus == 3) {
      return 0;
    } else {
      int result = 0;
      if (n % 3 == 0 && numberOfPlus >= 2) {
        result += recur(n / 3, numberOfPlus - 2);
      }
      result += recur(n - 1, numberOfPlus + 1);
      return result;
    }
  }

  int solution(int n) {
    if (n % 2 == 0)
      return 0;

    int answer = 0;
    answer = recur(n - 2, 2);
    return answer;
  }
}
