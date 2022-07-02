import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

public class ListaCarti extends JFrame{
 
    private int p;
    private double sumTotala=0;
    private JButton button1,button2,button3,button4,button5,button6,button7;
    private JButton b1,b2,b3,b4,b5,b6;
    private Carte[] catalog= new Carte[6];
    private StringBuffer sbc1 = new StringBuffer();
    private StringBuffer sbc2 = new StringBuffer();
    private StringBuffer sbc3 = new StringBuffer();
    private StringBuffer sbc4 = new StringBuffer();
    private StringBuffer sbc5 = new StringBuffer();
    private StringBuffer sbc6 = new StringBuffer();
    private String input;
    private int result;
    private StringBuffer sb1;
    private int x;
    private String[] plata = {"Card","Cont bancar"};
    private String[] livrare = {"Livrare prin posta obisnuita","Livrare prin posta rapida"};
    //private TreeSet<Carte> carti = new TreeSet<Carte>();
    public ListaCarti()
    {
        catalog[0]= new InteligentaEmotionala("Gilles Corcos & Corinne Vilder","\"Cum sa-ti dezvolti inteligenta emotionala\"",2019,224,24,34.90);
        catalog[1]= new Mister("Dan Brown","\"Codul lui Da Vinci\"",2013,512,48,37.99);
        catalog[2]= new Mister("Stephen King","\"Misery\"",1987,420,12,44);
        catalog[3]= new Thriller("Stephen King","\"Mr. Mercedes\"",2015,488,24,43.25);
        catalog[4]= new Thriller("Mo Hayder","\"Omul-Pasare\"",2008,384,15,47);
        catalog[5]= new Mister("Rodica Ojog-Brasoveanu","\"320 de pisici negre\"",2019,280,24,45);
        /*Carte c1 = new InteligentaEmotionala("Gilles Corcos & Corinne Vilder","\"Cum sa-ti dezvolti inteligenta emotionala\"",2019,224,24,34.90);
        Carte c2 = new Mister("Dan Brown","\"Codul lui Da Vinci\"",2013,512,48,37.99);
        Carte c3 = new Mister("Stephen King","\"Misery\"",1987,420,12,44);
        Carte c4 = new Thriller("Stephen King","\"Mr. Mercedes\"",2015,488,24,43.25);
        Carte c5 = new Thriller("Stephen King","\"Mr. Mercedes\"",2015,488,24,43.25);
        Carte c6 = new Thriller("Mo Hayder","\"Omul-Pasare\"",2008,384,15,47);
        carti.add(c1);
        carti.add(c2);
        carti.add(c3);
        carti.add(c4);
        carti.add(c5);
        carti.add(c6);
        */
        
        this.setTitle("Books");
        this.setLayout(new GridLayout(7,3,30,10));
        
        this.add(new JLabel(" \"Cum sa-ti dezvolti inteligenta emotionala\" "));
        button1=new JButton("Detalii");
        add(button1);
        b1=new JButton("Recenzii");
        add(b1);
        
        this.add(new JLabel(" \"Codul lui Da Vinci\" "));
        button2=new JButton("Detalii");
        add(button2);
        b2=new JButton("Recenzii");
        add(b2);
        
        this.add(new JLabel(" \"Misery\" "));
        button3=new JButton("Detalii");
        add(button3);
        b3=new JButton("Recenzii");
        add(b3);
        
        this.add(new JLabel(" \"Mr. Mercedes\" "));
        button4=new JButton("Detalii");
        add(button4);
        b4=new JButton("Recenzii");
        add(b4);
        
        this.add(new JLabel(" \"Omul-Pasare\" "));
        button5=new JButton("Detalii");
        add(button5);
        b5=new JButton("Recenzii");
        add(b5);
        
        this.add(new JLabel(" \"320 de pisici negre\" "));
        button6=new JButton("Detalii");
        add(button6);
        b6=new JButton("Recenzii");
        add(b6);
        
        button7=new JButton("Cos");
        add(button7);
        
        setSize(800,350);
        setLocationRelativeTo(null);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        sb1= new StringBuffer();
        
       button1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[0].toString(), "Cumparati?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[0].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "Ati adaugat in cos!");
                        sumTotala+=catalog[0].price;
                    }
            }
        });
        
        button2.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[1].toString(), "Cumparati?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[1].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "Ati adaugat in cos!");
                        sumTotala+=catalog[1].price;
                    }
            }
        });
        
         button3.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[2].toString(), "Cumparati?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[2].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "Ati adaugat in cos!");
                        sumTotala+=catalog[2].price;
                    }
            }
        });
         
          button4.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[3].toString(), "Cumparati?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[3].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "Ati adaugat in cos!");
                        sumTotala+=catalog[3].price;
                    }
            }
        });
          
         button5.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[4].toString(), "Cumparati?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[4].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "Ati adaugat in cos!");
                        sumTotala+=catalog[4].price;
                    }
            }
        });
          button6.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[5].toString(), "Cumparati?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[5].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "Ati adaugat in cos!");
                        sumTotala+=catalog[5].price;
                    }
            }
        });
           button7.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,"Finalizati cumparaturile?", "Cumparati?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION && sumTotala!=0)
                    {
                        
                        x = JOptionPane.showOptionDialog(null,sb1.toString()+ "\n In total aveti: "+String.format("%.2f",sumTotala)+"\n","Cos de cumparaturi",JOptionPane.DEFAULT_OPTION,JOptionPane.INFORMATION_MESSAGE,null,livrare,livrare[0]);
                       
                       if(x==0)
                       {
                           p = JOptionPane.showOptionDialog(null,"Tipul de livrare: Posta obisnuita.\n Cum doriti sa platiti comanda?","Mod de plata",JOptionPane.DEFAULT_OPTION,JOptionPane.INFORMATION_MESSAGE,null,plata,plata[0]);
                           if(p==0)
                           {
                               
                               new Card();
                           }
                           else
                               if(p==1)
                               {
                                   
                                   new ContBancar();
                               }
                       }
                       else
                           if(x==1)
                           {
                               p = JOptionPane.showOptionDialog(null,"Tipul de livrare: Posta rapida (comanda va fi livrata in 24 de ore).\n Cum doriti sa platiti comanda?","Mod de plata",JOptionPane.DEFAULT_OPTION,JOptionPane.INFORMATION_MESSAGE,null,plata,plata[0]);
                               
                               if(p==0)
                               {
                                   
                                   new Card();
                               }
                               else
                                   if(p==1)
                                   {
                                      
                                      new ContBancar(); 
                                   }
                           }
                    }
                    else{
                        if(sumTotala==0)
                            JOptionPane.showMessageDialog(null,"Sunteti sigur ca ati cumparat? Cosul de cumparaturi este gol!","Cos gol",JOptionPane.ERROR_MESSAGE);
                            
                    }
            }
        });
        sbc1.append("Recenzii: \n\n");
        sbc1.append(" Este o carte minunata!\n\n");
        sbc1.append(" M-a ajutat mult.\n\n");
        sbc1.append(" Interesanta carte!\n\n");
        sbc1.append(" Recomand cartea!\n\n");
        sbc1.append(" Mi-a placut cartea!\n\n");
        b1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    input = JOptionPane.showInputDialog(sbc1.toString()+"Vreti sa adaugati o recenzie?");
                        if(input != null)
                        {
                            sbc1.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Multumim pentru recenzie!","Recenzii",JOptionPane.INFORMATION_MESSAGE);
                            
                        }
            }
        
        });
        sbc2.append("Recenzii: \n\n");
        sbc2.append(" Mi-a placut enorm de mult cartea. Am stat mereu in suspans si incordare.\n\n");
        sbc2.append(" O carte buna si interesanta, cu o poveste captivanta.\n\n");
        sbc2.append(" Interesanta carte, merita citit!\n\n");
        sbc2.append(" Destul de captivant!\n\n");
        sbc2.append(" E una din cartile mele favorite!\n\n");
        b2.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    input = JOptionPane.showInputDialog(sbc2.toString()+"Vreti sa adaugati o recenzie?");
                    if(input != null)
                    {
                            sbc2.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Multumim pentru recenzie!","Recenzii",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        sbc3.append("Recenzii: \n");
        sbc3.append(" Am citit-o cu sufletul la gura!\n\n");
        sbc3.append(" Interesant subiectul.\n\n");
        sbc3.append(" Terifianta poveste!\n\n");
        sbc3.append(" Destul de captivant!\n\n");
        sbc3.append(" Cea mai buna carte scrisa de Stephen King!\n\n");
        b3.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                     input = JOptionPane.showInputDialog(sbc3.toString()+"Vreti sa adaugati o recenzie?");
                    if(input != null)
                    {
                            sbc3.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Multumim pentru recenzie!","Recenzii",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        sbc4.append("Recenzii: \n\n");
        sbc4.append(" O carte extraordinar de fantastică!! \nStephen King este unul dintre autorii care nu mă dezamăgește niciodată. \nIar Bill Hodges este un nou personaj de carte preferat al meu!!!\n\n");
        sbc4.append(" Mr. Mercedes are o deschidere care simbolizează măiestria caracterului lui Stephen King.\n\n");
        sbc4.append(" Am decis să citesc „Mr. Mercedes” de Stephen King după ce un prieten mi l-a recomandat.\n\n");
        sbc4.append(" Am avut grijă să aleg o carte a autorului meu preferat ca prima mea lectură a anului si nu regret alegerea\n\n");
        sbc4.append(" MR. MERCEDES de SPEPHEN KING a fost un roman polițist/de mister plin de acțiune,\n în ritm rapid și foarte plăcut, care mi-a susținut interesul de la început până la sfârșit.\n\n");
        b4.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                     input = JOptionPane.showInputDialog(sbc4.toString()+"Vreti sa adaugati o recenzie?");
                    if(input != null)
                    {
                            sbc4.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Multumim pentru recenzie!","Recenzii",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        sbc5.append("Recenzii: \n\n");
        sbc5.append(" Hayder face o treabă fantastică în dezvoltarea personajelor ei.\n\n");
        sbc5.append(" Omul-Pasare are loc în zorii noului mileniu și urmărește echipa de crimă a Poliției Metropolitane din Londra în timp ce încearcă să dea de urma unui posibil criminal în serie Jack the Ripper.\n Este chiar faina cartea!\n\n");
        sbc5.append(" Am așteptat momentul potrivit pentru a citi Omul-Pasare de ani de zile și, în sfârșit, mi-am făcut timp luna trecută – și această carte a fost intensă.\n\n");
        sbc5.append(" Wow. Această carte este foarte întunecată, răsucită și captivantă.\n\n");
        sbc5.append(" Aceasta carte este un thriller înfricoșător, captivant de la prima până la ultima pagină.\n\n");
        b5.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    input = JOptionPane.showInputDialog(sbc5.toString()+"Vreti sa adaugati o recenzie?");
                    if(input != null)
                    {
                            sbc5.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Multumim pentru recenzie!","Recenzii",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        sbc6.append("Recenzii: \n\n");
        sbc6.append(" Ei bine, a fost for-mi-da-bi-lă!\n\n");
        sbc6.append(" Melania este magnifica in 320 de pisici negre.M-am trezit placut surprinsa de aventurile ei si am ras cu pofta.Este cu siguranta un personaj captivant.\n\n");
        sbc6.append(" Mult prea tare, citesc si rad cu lacrimi la propriu, demult nu am mai citit o carte care sa ma scoata pur si simplu din cotidian si sa-mi dea o stare de bine incredibila.\n\n");
        sbc6.append(" Trebuie să menționez că titlul acestui roman m-a intrigant. Mi-a dat năbădăi și mă întrebam : ce or fi făcând 320 de pisici negre toate la un loc?\n\n");
        sbc6.append(" Cel mai reușit roman al seriei și oricum unul dintre primele trei cele mai bune ale autoarei. Nici nu știu dacă cele 320 de pisici sunt un roman polițist, sau mai mult o parodie.\n\n");
        b6.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    input = JOptionPane.showInputDialog(sbc6.toString()+"Vreti sa adaugati o recenzie?");
                    if(input != null)
                    {
                            sbc6.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Multumim pentru recenzie!","Recenzii",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        
    }
    
}
