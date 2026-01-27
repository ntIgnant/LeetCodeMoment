import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class CableCar {

    // This function was dome with assis of chatgpt
    static boolean allowPlacement(double d, int p, double u, double v, double testDist){

        double latest_pos = 0.0;
        int posi = 1; // initial possition at 0

        // p is the number of posts
        while (posi < p) {
            double next_pos = latest_pos + testDist; // current (allowed) next possition for the placement

            // If statement to avoid the placement in the forbiden area "range(u, v)"
            if(next_pos > u && next_pos < v){
                next_pos = v;
            }

            if(next_pos > d){
                return false; // goes beyond the boundaries | d is the distance/length of the 'cable'
            }

            // Upldate the positions
            latest_pos = next_pos;
            posi++;
        }

        return true;
    }
    
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line_numCases = br.readLine();

        StringTokenizer input_str_numCases = new StringTokenizer(line_numCases);

        // Transform the gotten chunck of data (separated by spaces) into an int
        int numCases = Integer.parseInt(input_str_numCases.nextToken());


        for(int i = 0; i < numCases; i++){
            // Get the numbers of each line (𝑑, 𝑝, 𝑢, and 𝑣) always 4 nums
            String line_case = br.readLine();
            StringTokenizer input_str_dpuv = new StringTokenizer(line_case);

            // Separate the numbers from the input line
            int d = Integer.parseInt(input_str_dpuv.nextToken()); // Total distance
            int p = Integer.parseInt(input_str_dpuv.nextToken()); // Number of posts
            int u = Integer.parseInt(input_str_dpuv.nextToken()); // start-point forbiden range
            int v = Integer.parseInt(input_str_dpuv.nextToken()); // finish-point forbiden range

            // Binary search to look for thhe maximum "best" distances between the posts within the range of thhe length of the cable
            // And test if it is possible to place all the posts, without putting them in the forbiden area (range(u, v))
            double minimal = 0.0; // min distance
            double maximal = d; // max distance
            int depth = 70; // number of iterations that the binary searchh can have in order to get good enogh accuracy | "maximal minimum distance between two posts that can be achieved with an absolute error of up to 10^−4" | got the explanation fo the logic from chatgpt

            for(int j = 0; j < depth; j++){
                double middle = (minimal + maximal) / 2.0;

                if(allowPlacement(d, p, u, v, middle)){
                    minimal = middle;
                }
                else{
                    maximal = middle;
                }
            }

            System.out.printf("Case #%d: %.10f%n", i+1, minimal); // Got the formating way from chatgpt

        }
    }
}
