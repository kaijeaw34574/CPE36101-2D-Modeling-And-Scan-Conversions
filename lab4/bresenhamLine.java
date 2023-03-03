/* Lab4: Bresenham's line algorithm
 */
import java.util.*;
import java.lang.Math;

public class bresenhamLine {
    
    /* Find points for create line pixel form point(x0 ,y0) to point(x1, y1) 
     * by used Bresenham's line algorithm for all cases
     */
    public static void bresenhamLine(int x0, int y0, int x1, int y1) {
        int dx = Math.abs(x1 - x0);
        int dy = Math.abs(y1 - y0);
        int d = dy - dx;
        int slidingX = 0;
        int slidingY = 0;
        int dCondition = 0;
        boolean checkEnd = false;
        /* Sliding points x and y form input */
        if (x0 < x1)
            slidingX = 1;
        else
            slidingX = -1;
        if (y0 < y1)
            slidingY = 1;
        else
            slidingY = -1;
        /* Loop for check condition if the condition is true give sliding 
         * point x0 and y0 follow by given
         */
        while (checkEnd == false) {
            System.out.format("(%d, %d)\n", x0, y0);
            if ((x0 == x1) && (y0 == y1)) 
                checkEnd = true;
            dCondition = 2 * d;
            if (dCondition < dy) {
                d = d + dy;
                x0 += slidingX;
            }
            if (dCondition > -dx) {
                d = d - dx;
                y0 += slidingY;
            }
        }
    }
    
    /* Main function get input point(x0, y0) to point(x1, y1) from user
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        int x0 = sc.nextInt(); 
        int y0 = sc.nextInt(); 
        int x1 = sc.nextInt(); 
        int y1 = sc.nextInt();  
        bresenhamLine(x0, y0, x1, y1);
        sc.close();
    }
}
