/* Lab2: Line Clipping
 */
import java.util.*;

public class lab2 {
    
    /* Defining region codes */ 
    static final int INSIDE = 0;  // 0000
    static final int LEFT = 1;    // 0001
    static final int RIGHT = 2;   // 0010
    static final int BOTTOM = 4;  // 0100
    static final int TOP = 8;     // 1000

    /* Defining x_max, y_max and x_min, y_min for
     * clipping rectangle. Since diagonal points are
     * enough to define a rectangle
     */
    static final int x_min = 10;
    static final int y_min = 10;
    static final int x_max = 260;
    static final int y_max = 160;
    
    /* Function to compute region code for a point(x, y) */
    static int computeCode(double x, double y) {
        int code = INSIDE;
        if (x < x_min) 
            code |= LEFT;
        else if (x > x_max) 
            code |= RIGHT;
        if (y < y_min) 
            code |= BOTTOM;
        else if (y > y_max) 
            code |= TOP;
        return code;
    }
    
    /* Function to generate the four-bit code for point(x, y) */
    static int[] bitCode(double x, double y) {
        int[] fourBit = {0, 0, 0, 0};
        if (y > y_max)
            fourBit[0] = 1;
        if (y < y_min)
            fourBit[1] = 1;
        if (x > x_max)
            fourBit[2] = 1;
        if (x < x_min)
            fourBit[3] = 1;
        return fourBit;
    }

    /* Implementing Cohen-Sutherland algorithm
     * Clipping a line from P1 = (x2, y2) to P2 = (x2, y2)
     */
    static void cohenSutherlandClip(double x1, double y1, double x2, double y2) {
        int code1 = computeCode(x1, y1);
        int code2 = computeCode(x2, y2);
        int accept = 0;
        int checkType = 0;
        while (accept == 0) {
            if ((code1 == 0) && (code2 == 0)) {
                accept = 1;
                break;
            }
            else if ((code1 & code2) != 0) {
                break;
            }
            else {
                int code_out = 0;
                double x = 0, y = 0;
                if (code1 != 0)
                    code_out = code1;
                else
                    code_out = code2;
                /* Find intersection point 
                 * using formulas y = y1 + slope * (x - x1), x = x1 + (1 / slope) * (y - y1)
                 */
                if ((code_out & TOP) != 0) {
                    x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1);
                    y = y_max;
                }
                else if ((code_out & BOTTOM) != 0) {
                    x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1);
                    y = y_min;
                }
                else if ((code_out & RIGHT) != 0) {
                    y =  y1 + (y2 - y1) * (x_max - x1) / (x2 - x1);
                    x = x_max;
                }
                else if ((code_out & LEFT) != 0) {
                    y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1);
                    x = x_min;
                }
                checkType = 1; // If it passes here, it means that it is Clipping Candidate
                if (code_out == code1) {
                    x1 = x;
                    y1 = y;
                    code1 = computeCode(x1, y1);
                }
                else {
                    x2 = x;
                    y2 = y;
                    code2 = computeCode(x2, y2);
                }
            }
        }
        if (code1 == 0 && code2 == 0 && checkType == 0) {
            System.out.println("Visible");
            System.out.format("(%.3f, %.3f)" + "\n", x1, y1);
            System.out.format("(%.3f, %.3f)" + "\n", x2, y2);
        }
        else if ((code1 & code2) != 0) {
            System.out.println("Invisible");
        }
        else {
            System.out.println("Clipping Candidate");
            System.out.format("(%.3f, %.3f)" + "\n", x1, y1);
            System.out.format("(%.3f, %.3f)" + "\n", x2, y2);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        double x1 = sc.nextDouble(); 
        double y1 = sc.nextDouble(); 
        double x2 = sc.nextDouble(); 
        double y2 = sc.nextDouble();  
        int[] bitCode1 = bitCode(x1, y1);
        int[] bitCode2 = bitCode(x2, y2);
        System.out.println(bitCode1[0] + " " + bitCode1[1] + " " + bitCode1[2] + " " + bitCode1[3]);
        System.out.println(bitCode2[0] + " " + bitCode2[1] + " " + bitCode2[2] + " " + bitCode2[3]);
        cohenSutherlandClip(x1, y1, x2, y2);
        sc.close();
    }
}