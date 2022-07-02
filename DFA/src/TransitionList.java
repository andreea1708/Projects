import java.util.*;
class TransitionList {
    private ArrayList<Transition> list;
    TransitionList(){ this.list=new ArrayList<Transition>();}
    void addTransition(Transition tr){this.list.add(tr);}
    Transition getTransition(String start_state,char symbol)
    {
        Transition tmp=null;
        for(int i=0;i<this.list.size();i++)
        {
            tmp=this.list.get(i);
            if(tmp.getStState().equals(start_state)&&tmp.getSymbol()==symbol)
                return tmp;
        }
        return tmp;
    }
    public void print_tl()
    {
        for(int i=0;i<list.size();i++){
            System.out.println(list.get(i).getStState()+" "+list.get(i).getSymbol()+" "+list.get(i).getEndState());
        }
    }
  }
