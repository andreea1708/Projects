
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
        sb.append("Author: "+autor+"\n");
        sb.append("Title: "+titlu+"\n");
        sb.append("Year of publication: "+anAparitiei+"\n");
        sb.append("Number of pages: "+nrPag+"\n");
        sb.append("Price: "+price+"\n");
        sb.append("Delivery period: "+perioadaDeLivrare+" ore\n");
        return sb.toString();
    }
}
