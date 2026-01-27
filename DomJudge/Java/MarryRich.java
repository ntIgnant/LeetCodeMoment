import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class MarryRich {

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

    // Union-Find algorithm implementation
    // This was done with assis of AI (chatGPT)

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

    public static void main(String[] args) throws IOException {
        // Fast way to get data from input (this reads lines)
        BufferedReader buffRe = new BufferedReader(new InputStreamReader(System.in));

        String line_numCases = readNoBlank(buffRe);
        StringTokenizer input_str_numCas= new StringTokenizer(line_numCases); // This 'separates' the string input whenever there is a space

        // Transform the gotten chunck of data (separated by spaces) into an int
        int numCases = Integer.parseInt(input_str_numCas.nextToken()); // Number of Cases

        for(int i = 0; i < numCases; i++){

            // Get the a b c values (per case) | num people (including jacob), fam relations, marriage relations
            String line1 = readNoBlank(buffRe);
            StringTokenizer input_str_abc = new StringTokenizer(line1); // Create a new reader for the 'abc' line
            int a = Integer.parseInt(input_str_abc.nextToken());
            int b = Integer.parseInt(input_str_abc.nextToken()); // num of family relations
            int c = Integer.parseInt(input_str_abc.nextToken()); // num of mariage relations

            union_find(a); // initialization for union_find

            // Get the money of each person (money line)
            int[] moneys = new int[a+1];
            int idx = 1;

            while (idx <= a - 1) {
                String line = readNoBlank(buffRe);
                if (line == null) break;
                StringTokenizer st = new StringTokenizer(line);
                while (st.hasMoreTokens() && idx <= a - 1) {
                    moneys[idx++] = Integer.parseInt(st.nextToken());
                }
            }

            // Read the total relations (family and marriage relations)

            // Read FAMILY relations and find union of those
            for(int j = 0; j < b; j++){
                StringTokenizer input_st_famRela = new StringTokenizer(readNoBlank(buffRe));
                int person1 = Integer.parseInt(input_st_famRela.nextToken());
                int person2 = Integer.parseInt(input_st_famRela.nextToken());

                // look for its union (fam relation)
                union(person1, person2);
            }

            // Read the MARRIAGE relations
            boolean[] is_married = new boolean[a + 1];
            for(int m = 0; m < c; m++){
                StringTokenizer input_st_marryRela = new StringTokenizer(readNoBlank(buffRe));
                int person_ma1 = Integer.parseInt(input_st_marryRela.nextToken());
                int person_ma2 = Integer.parseInt(input_st_marryRela.nextToken());

                is_married[person_ma1] = true;
                is_married[person_ma2] = true;

                union(person_ma1, person_ma2);
            }

            // Go though all the persons (moneys) and find the best one that is not in the union_find relation
            int rootJakob = find(a);
            int best = -1;

            for (int person = 1; person <= a - 1; person++) {
                if (!is_married[person] && find(person) != rootJakob) {
                    best = Math.max(best, moneys[person]);
                }
            }

            if (best == -1) {
                System.out.println("Case #" + (i + 1) + ": impossible");
            } else {
                System.out.println("Case #" + (i + 1) + ": " + best);
            }

        }
    }
}