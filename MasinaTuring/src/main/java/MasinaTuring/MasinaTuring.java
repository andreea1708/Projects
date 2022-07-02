package MasinaTuring;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class MasinaTuring {

    public String stareCurenta;
    public String[] stariFinale;
    public String[] alfabet;
    public ArrayList<Tranzitie> listaTranzitii = new ArrayList<>();
    public int cursor = 0;

    MasinaTuring(String numeFisier) {
        BufferedReader buf;
        try {
            buf = new BufferedReader(new FileReader(numeFisier));

            stareCurenta = buf.readLine();

            stariFinale = buf.readLine().split(" ");

            alfabet = buf.readLine().split(" ");

           
            String tranzitie;
            while (true) {
                tranzitie = buf.readLine();
                if (tranzitie == null) {
                    break;
                }

                String[] box = tranzitie.split(" "); //stocam informatiile de tranzitie
                Tranzitie t = new Tranzitie(box[0], box[1].charAt(0), box[2], box[3].charAt(0), box[4].charAt(0));//un obiect Tranzitie care salveaza componentele tranzitiei
                listaTranzitii.add(t);
            }
            buf.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String cuvantNou(Tranzitie t, String cuvant) {
        String cuvantNou = cuvant.substring(0, cursor) + t.getSimbolFinal() + cuvant.substring(cursor + 1, cuvant.length());
        return cuvantNou;

    }//aabb  Babb BabbB BabBB BBbBB BBBB

    public boolean existaDrum(ArrayList<Tranzitie> lista, String cuvant) {
        boolean avemDrum = false;
        for (int i = 0; i < lista.size(); i++) {
            Tranzitie t = lista.get(i);
            if (stareCurenta.equals(t.getStareInitiala()) && cuvant.charAt(cursor) == t.getSimbolInitial()) {
                avemDrum = true;
            }
        }
        return avemDrum;
    }

    public boolean algoritm(String cuvant) {
        int poz;
        cuvant = "B" + cuvant;

        while (true) {
            for (int i = 0; i < listaTranzitii.size(); i++) {
                if (cursor < 0) { //se asigura ca nu sare cursor 
                    return false;
                }
                if (cursor == cuvant.length()) {
                    cuvant = cuvant + "B";
                }
                Tranzitie t = listaTranzitii.get(i);
                if (existaDrum(listaTranzitii, cuvant)) {
                    if (stareCurenta.equals(t.getStareInitiala()) && cuvant.charAt(cursor) == t.getSimbolInitial()) {
                        stareCurenta = t.getStareFinala();
                        System.out.println();       
                        System.out.println("Traseul: "+t.getStareInitiala()+" "+t.getDirectie()+" "+t.getStareFinala()+" "+t.getSimbolInitial()+" "+t.getSimbolFinal());
                        cuvant = cuvantNou(t, cuvant);
                        System.out.println(cuvant + " - " + stareCurenta);
                        for( poz=0;poz<cuvant.length();poz++)
                        {
                            if(poz!=cursor)
                                System.out.print(" ");
                            else
                                System.out.print("^");
                        }
                        
                        if (t.getDirectie() == 'L') {
                            cursor--;
                        } else {
                            cursor++;
                        }
                        break;
                    }
                } else {
                    return false;
                }
            }

            for (int i = 0; i < stariFinale.length; i++) {
                if (stareCurenta.equals(stariFinale[i])) {
                    return true;
                }
            }
        }
    }
}
