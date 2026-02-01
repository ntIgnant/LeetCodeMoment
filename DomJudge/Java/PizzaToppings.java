import java.io.BufferedReader;
import java.io.IOException;

public class PizzaToppings {

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

    public static void main(String args[]) throws IOException{
        

    }
}