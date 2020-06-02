import java.io.*;
import java.util.*;
public class Solution {

  public static boolean checkRoom(int newOwner, int roomType, int[] used,
                                  int[] owner, int index, int leftBound,
                                  int rightBound) {
    if (index >= rightBound || index < leftBound)
      return false;
    if (owner[index] == newOwner)
      return true;
    if ((used[index] | roomType) == used[index]) {
      // System.out.println("newOwner is Wrong!: " + (char)newOwner);
      return false;
    } else
      return true;
  }
  public static void changeRoom(int newOwner, int roomType, int[] used,
                                int[] owner, int index) {
    if (index >= owner.length || index < 0)
      return;

    owner[index] = newOwner;
    used[index] |= roomType;
  }

  public static int findCapitalLeft(char[] charArr, int index) {
    if (index < 0 || (!SmallCheck(charArr[index])))
      return index;
    else
      return findCapitalLeft(charArr, index - 1);
  }
  public static int findCapitalRight(char[] charArr, int index) {
    if (index >= charArr.length || (!SmallCheck(charArr[index])))
      return index;
    else
      return findCapitalRight(charArr, index + 1);
  }

  public static boolean checkType1(char key, int[] used, int[] owner,
                                   char[] charArr,
                                   ArrayList<Integer> indexList) {
    int newOwner = (int)key;
    for (int i = 0; i < indexList.size(); i++) {
      int index = indexList.get(i);
      int leftBound = (i == 0) ? 0 : indexList.get(i - 1);
      int rightBound =
          (i == (indexList.size() - 1)) ? charArr.length : indexList.get(i + 1);
      int leftIndex = findCapitalLeft(charArr, index);
      int rightIndex = findCapitalRight(charArr, index);

      if (checkRoom(newOwner, 1, used, owner, leftIndex, leftBound, rightBound))
        changeRoom(newOwner, 1, used, owner, leftIndex);
      else
        return false;
      if (checkRoom(newOwner, 1, used, owner, rightIndex, leftBound,
                    rightBound))
        changeRoom(newOwner, 1, used, owner, rightIndex);
      else
        return false;
    }
    return true;
  }
  public static boolean checkType2(char key, int[] used, int[] owner,
                                   char[] charArr,
                                   ArrayList<Integer> indexList) {
    int newOwner = (int)key;
    for (int i = indexList.get(0) + 1; i < indexList.get(1); i++) {

      if (!SmallCheck(charArr[i])) {
        if (checkRoom(newOwner, 2, used, owner, i, 0, charArr.length))
          changeRoom(newOwner, 2, used, owner, i);
        else
          return false;
      }
    }
    return true;
  }
  public static boolean checkType3(char key, int[] used, int[] owner,
                                   char[] charArr,
                                   ArrayList<Integer> indexList) {
    int newOwner = (int)key;
    int leftIndex = findCapitalLeft(charArr, indexList.get(0));
    int middleIndex = findCapitalRight(charArr, indexList.get(0));
    int rightIndex = findCapitalRight(charArr, indexList.get(1));
    // try checkType 1
    if (checkRoom(newOwner, 1, used, owner, leftIndex, 0, charArr.length) &&
        checkRoom(newOwner, 1, used, owner, middleIndex, 0, charArr.length) &&
        checkRoom(newOwner, 1, used, owner, rightIndex, 0, charArr.length)) {
      changeRoom(newOwner, 1, used, owner, leftIndex);
      changeRoom(newOwner, 1, used, owner, middleIndex);
      changeRoom(newOwner, 1, used, owner, rightIndex);
    } else {
      if (checkRoom(newOwner, 2, used, owner, middleIndex, 0, charArr.length))
        changeRoom(newOwner, 2, used, owner, middleIndex);
      else
        return false;
    }
    return true;
  }

  public static ArrayList<String> getStringList(int[] owner, char[] charArr) {

    int preOwner = -1;

    ArrayList<String> result = new ArrayList<String>();
    ArrayList<Character> temp = new ArrayList<Character>();

    for (int i = 0; i < charArr.length; i++) {
      char ch = charArr[i];

      if (!SmallCheck(ch)) {
        if (preOwner == -1)
          temp.add(ch);
        else if (preOwner == owner[i])
          temp.add(ch);
        else {
          result.add(getStringRepresenation(temp));
          temp.clear();
          temp.add(ch);
        }
        preOwner = owner[i];
      }
    }

    result.add(getStringRepresenation(temp));
    return result;
  }

  public static String getStringRepresenation(ArrayList<Character> list) {
    StringBuilder builder = new StringBuilder(list.size());
    for (char ch : list) {
      builder.append(ch);
    }
    return builder.toString();
  }

  public static boolean SmallCheck(char ch) {
    if ((97 <= (int)ch) && ((int)ch <= 122))
      return true;
    else
      return false;
  }

  public static int getType(char key, char[] charArr,
                            Hashtable<Character, ArrayList<Integer>> ht) {
    int size = ht.get(key).size();
    if (size == 1)
      return 1;
    else if (size == 2) {
      int startPoint = ht.get(key).get(0);
      int endPoint = ht.get(key).get(1);
      int cnt = 0;
      for (int i = startPoint + 1; i < endPoint; i++) {
        if (!SmallCheck(charArr[i]))
          cnt++;
      }
      if (cnt == 0)
        return 0;
      else if (cnt == 1) {
        return 3;
      } else
        return 2;
    } else
      return 1;
  }

  public static String solution(String sentence) {

    boolean vld = true;
    int L = sentence.length();

    char[] charArr = sentence.toCharArray();
    Hashtable<Character, ArrayList<Integer>> ht =
        new Hashtable<Character, ArrayList<Integer>>();
    int[] used = new int[L];
    int[] owner = new int[L];

    for (int i = 0; i < charArr.length; i++) {
      char ch = charArr[i];
      if (SmallCheck(ch)) {
        if (ht.get(ch) != null)
          ht.get(ch).add(i);
        else {
          ArrayList<Integer> temp = new ArrayList<Integer>();
          temp.add(i);
          ht.put(ch, temp);
        }
      }
    }
    // debug
    // for (Map.Entry m : ht.entrySet()) {
    //   System.out.println(m.getKey() + " " + m.getValue());
    // }

    ArrayList<Character> keysList = new ArrayList<Character>(ht.keySet());

    for (char key : keysList) {
      int ttype = getType(key, charArr, ht);
      // System.out.println("ttype: " + ttype);

      switch (ttype) {
      case 0:
        // System.out.println("newOwner is Wrong!: " + key);
        vld &= false;
        break;
      case 1:
        vld &= checkType1(key, used, owner, charArr, ht.get(key));
        break;
      case 2:
        vld &= checkType2(key, used, owner, charArr, ht.get(key));
        break;
      case 3:
        vld &= checkType3(key, used, owner, charArr, ht.get(key));
        break;
      }
      // System.out.println("key: " + key);
      // System.out.println("vld: " + vld);
    }
    // System.out.println("owner: " + Arrays.toString(owner));

    if (!vld)
      return "invalid";
    else
      return String.join(" ", getStringList(owner, charArr));
  }

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String s = scan.nextLine();

    System.out.println(solution(s));
    scan.close();
  }
}
