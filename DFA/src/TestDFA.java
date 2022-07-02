
public class TestDFA {

    public static void main(String[] args) throws Exception {
        Automaton M = new Automaton("D:\\Ore_facultate\\An_2\\Limbaje_formale_si_compilatoare\\Proiect1\\src\\M.txt");
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
         * Alte exemple
         * System.out.println("Alte exemple:");
         * System.out.println(M.analyze("aa"));
         * System.out.println(M.analyze("cc"));
         * System.out.println(M.analyze("bbbbbbbab"));
          System.out.println(M.analyze(" "));
         * System.out.println(M.analyze("aya"));
         */
    }

}
