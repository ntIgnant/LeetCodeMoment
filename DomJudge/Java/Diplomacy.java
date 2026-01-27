import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Diplomacy {

    // Function to read line from input and skip the blank line (each new case)
    static String readNoBlank(BufferedReader br) throws IOException {
        String line;
        while ((line = br.readLine()) != null) {
            if (!line.trim().isEmpty()){
                return line; // skip blank lines
            }
        }
        return null;
    }


    // Unfion-Find function (Needs to be fixed/modded to work with the parity bit)
    static int[] parent;
    static int[] size;

    static void union_find(int n){
        parent = new int[n + 1];
        size = new int[n + 1];

        for(int i = 1; i <= n; i++){
            parent[i] = i;
            size[i] = 1;
        }
    }

    static int find(int a) {
        int current = a;

        while (true) {
            int p = parent[current];
            if (p == current) break;
            current = p;
        }

        int root = current;
        current = a;

        while (current != root) {
            int p = parent[current];
            parent[current] = root;
            current = p;
        }

        return root;
    }

    static void union(int x, int y) {
        int a = find(x);
        int b = find(y);

        if (a == b) return;

        if (size[a] < size[b]) {
            int tmp = a;
            a = b;
            b = tmp;
        }

        parent[b] = a;
        size[a] += size[b];
    }

    public static void main(String args[]) throws IOException{
        BufferedReader buffRe = new BufferedReader(new InputStreamReader(System.in));
        
        String line_numCases = readNoBlank(buffRe);
        StringTokenizer str_numCases = new StringTokenizer(line_numCases);
        int numCases = Integer.parseInt(str_numCases.nextToken()); // number of cases from input (as int)

        for(int i =0; i < numCases; i++){

            // First, get the two values (n and m)
            String line1 = readNoBlank(buffRe);
            StringTokenizer input_str_nm = new StringTokenizer(line1); // n and m line

            // Separate the values and assign to variables
            int n = Integer.parseInt(input_str_nm.nextToken()); // n "number of countries, so 1 - n"
            int m = Integer.parseInt(input_str_nm.nextToken()); // m "number of interactions between countries"

            for(int j = 0; j < m; j++){
                // Iterate though all the country relations, each line contains (relaType, country1, country2)
                String line_relation = buffRe.readLine();
                StringTokenizer input_str_relation = new StringTokenizer(line_relation);
                char R = input_str_relation.nextToken().charAt(0); // Get the type of relation as charactyer | this can be either F (friendship) or A (Antipathy)
                int x = Integer.parseInt(input_str_relation.nextToken());
                int y = Integer.parseInt(input_str_relation.nextToken());



            }
        }
    }
}