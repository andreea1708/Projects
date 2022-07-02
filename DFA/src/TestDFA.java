import java.io.File;
public class TestDFA {

    public static void main(String[] args) throws Exception {
        String currentPath = new File("").getAbsolutePath();
        Automaton M=new Automaton(currentPath + "\\src\\M.txt");
        M.printAutomaton();
        String w1 = "aaab";// true
        String w2 = "abbc";// false
        String w3 = "";// true
        String w4 = "baaac";// false
        System.out.println(M.analyze(w1));
        System.out.println(M.analyze(w2));
        System.out.println(M.analyze(w3));
        System.out.println(M.analyze(w4));
        /*
         * Other examples
         * System.out.println("Other examples:");
         * System.out.println(M.analyze("aa"));
         * System.out.println(M.analyze("cc"));
         * System.out.println(M.analyze("bbbbbbbab"));
          System.out.println(M.analyze(" "));
         * System.out.println(M.analyze("aya"));
         */
    }

}
