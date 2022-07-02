 class Transition {
    private String start_state;
    private char symbol;
    private String end_state;
    Transition(String start_state,char symbol,String end_state)
    {
        this.start_state=start_state;
        this.symbol=symbol;
        this.end_state=end_state;
    }
    String getStState(){return this.start_state;}
    char getSymbol(){return this.symbol;}
    String getEndState(){return this.end_state;}
}
