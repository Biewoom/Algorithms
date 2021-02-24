import UserDefined.ParsingString;
import java.util.*;

public class accessmodifierCheck {
  private int a = 5;
  public int b = 10;
  protected int c = 15;

  public static void main(String[] args) {
    System.out.println("hello world!");
    ParsingString.sayHello();
    int[] test = new int[5];

    System.out.println("test: " + test[6]);
  }
}
