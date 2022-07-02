import java.io.BufferedReader;
import java.io.FileReader;

class Automaton {
    private String initial_state;
    private String final_states[];
    private TransitionList tl = new TransitionList();

    Automaton(String file) throws Exception {
        try (BufferedReader buf = new BufferedReader(new FileReader(file))) {
            this.initial_state = buf.readLine();
            this.final_states = buf.readLine().split(" ");
            while (true) {
                String tmp = buf.readLine();
                if (tmp == null)
                    break;
                else {
                    String tbl[] = tmp.split(" ");
                    Transition tr = new Transition(tbl[0], tbl[1].charAt(0), tbl[2]);
                    tl.addTransition(tr);

                }
            }
        }

    }

    boolean analyze(String w) {
        String current_state = initial_state;
        System.out.print(current_state+" ");
        for (int i = 0; i < w.length(); i++) {
            Transition temp = tl.getTransition(current_state, w.charAt(i));
            if (temp != null) {
                current_state = temp.getEndState();
                if (i == w.length() - 1) {
                    return isFinalState(temp.getEndState());
                }
            }
            System.out.print(current_state+" ");
        }
        return isFinalState(current_state);
    }

    boolean isFinalState(String state) {
        for (int j = 0; j < final_states.length; j++) {
            if (final_states[j].equals(state)) {
                return true;
            }
        }
        return false;
    }

    void printAutomaton() {

        System.out.println(initial_state);
        for (int i = 0; i < final_states.length; i++)
            System.out.println(final_states[i] + " ");
        System.out.println('\n');
        tl.print_tl();
    }
}
