
public class Carte {
    private String autor, titlu;
    private int anAparitiei, nrPag;
    private int perioadaDeLivrare;
    protected double price;
    private StringBuffer sb;
    public Carte (String autor, String titlu, int anAparitie, int nrPag,int perioadaDeLivrare, double price){
        this.autor=autor;
        this.titlu=titlu;
        this.anAparitiei=anAparitie;
        this.nrPag=nrPag;
        this.perioadaDeLivrare=perioadaDeLivrare;
        this.price=price;
    }
    public String getAutor(){
        return autor;
    }
    public String getTitlu(){
        return titlu;
    }
    public int getAnAparitie(){
        return anAparitiei;
    }
    public int getNrPag(){
        return nrPag;
    }
    public int getPerioadaDeLivrare(){
        return perioadaDeLivrare;
    }
    public double getPrice(){
        return price;
    }
    public String toString(){
        sb=new StringBuffer();
        sb.append("Autorul: "+autor+"\n");
        sb.append("Titlu: "+titlu+"\n");
        sb.append("Anul aparitiei: "+anAparitiei+"\n");
        sb.append("Numaru de pagini: "+nrPag+"\n");
        sb.append("Pretul: "+price+"\n");
        sb.append("Perioada de livrare: "+perioadaDeLivrare+" ore\n");
        return sb.toString();
    }
}
