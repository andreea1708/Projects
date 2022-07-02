package MasinaTuring;
class Main{
    public static void main(String[] args) {
        MasinaTuring MT = new MasinaTuring("Turing.txt");
        if(MT.algoritm("aabbaa")){
            System.out.print("Cuvant acceptat");
        }
        else
            System.out.println("Nu este acceptat");
    }
}