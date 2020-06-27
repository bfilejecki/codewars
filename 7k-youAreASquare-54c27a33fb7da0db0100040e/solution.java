public class Square {    
    public static boolean isSquare(int n) {   
        if (n < 0) {
          return false;
        } else if (n == 0) {
          return true;
        } else {
          for (int i = 0; i <= n/2; i++) {
            if (i*i == n) {
              return true;
            }
          }
          return false;
        }
    }
}
