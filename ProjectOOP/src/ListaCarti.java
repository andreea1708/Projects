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

    public ListaCarti()
    {
        catalog[0]= new InteligentaEmotionala("Gilles Corcos & Corinne Vilder","\"Cum sa-ti dezvolti inteligenta emotionala\"",2019,224,24,34.90);
        catalog[1]= new Mister("Dan Brown","\"Codul lui Da Vinci\"",2013,512,48,37.99);
        catalog[2]= new Mister("Stephen King","\"Misery\"",1987,420,12,44);
        catalog[3]= new Thriller("Stephen King","\"Mr. Mercedes\"",2015,488,24,43.25);
        catalog[4]= new Thriller("Mo Hayder","\"Omul-Pasare\"",2008,384,15,47);
        catalog[5]= new Mister("Rodica Ojog-Brasoveanu","\"320 de pisici negre\"",2019,280,24,45);
        
        this.setTitle("Books");
        this.setLayout(new GridLayout(7,3,30,10));
        
        this.add(new JLabel(" \"Cum sa-ti dezvolti inteligenta emotionala\" "));
        button1=new JButton("Details");
        add(button1);
        b1=new JButton("Reviews");
        add(b1);
        
        this.add(new JLabel(" \"Codul lui Da Vinci\" "));
        button2=new JButton("Details");
        add(button2);
        b2=new JButton("Reviews");
        add(b2);
        
        this.add(new JLabel(" \"Misery\" "));
        button3=new JButton("Details");
        add(button3);
        b3=new JButton("Reviews");
        add(b3);
        
        this.add(new JLabel(" \"Mr. Mercedes\" "));
        button4=new JButton("Details");
        add(button4);
        b4=new JButton("Reviews");
        add(b4);
        
        this.add(new JLabel(" \"Omul-Pasare\" "));
        button5=new JButton("Details");
        add(button5);
        b5=new JButton("Reviews");
        add(b5);
        
        this.add(new JLabel(" \"320 de pisici negre\" "));
        button6=new JButton("Details");
        add(button6);
        b6=new JButton("Reviews");
        add(b6);
        
        button7=new JButton("Shopping cart");
        add(button7);
        
        setSize(800,350);
        setLocationRelativeTo(null);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        sb1= new StringBuffer();
        
       button1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[0].toString(), "Are you buying?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[0].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "You have added to your cart!");
                        sumTotala+=catalog[0].price;
                    }
            }
        });
        
        button2.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[1].toString(), "Are you buying?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[1].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "You have added to your cart!");
                        sumTotala+=catalog[1].price;
                    }
            }
        });
        
         button3.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[2].toString(), "Are you buying?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[2].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "You have added to your cart!");
                        sumTotala+=catalog[2].price;
                    }
            }
        });
         
          button4.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[3].toString(), "Are you buying?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[3].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "You have added to your cart!");
                        sumTotala+=catalog[3].price;
                    }
            }
        });
          
         button5.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[4].toString(), "Are you buying?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[4].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "You have added to your cart!");
                        sumTotala+=catalog[4].price;
                    }
            }
        });
          button6.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,catalog[5].toString(), "Are you buying?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION)
                    {
                        sb1.append(catalog[5].toString());
                        sb1.append("\n\n");
                        JOptionPane.showMessageDialog(null, "You have added to your cart!");
                        sumTotala+=catalog[5].price;
                    }
            }
        });
           button7.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    result=JOptionPane.showConfirmDialog(null,"Are you done shopping?", "Are you buying?",JOptionPane.YES_NO_OPTION);
                    if(result == JOptionPane.YES_OPTION && sumTotala!=0)
                    {
                        
                        x = JOptionPane.showOptionDialog(null,sb1.toString()+ "\n In total you have: "+String.format("%.2f",sumTotala)+"\n","Shopping cart",JOptionPane.DEFAULT_OPTION,JOptionPane.INFORMATION_MESSAGE,null,livrare,livrare[0]);
                       
                       if(x==0)
                       {
                           p = JOptionPane.showOptionDialog(null,"Delivery type: Ordinary mail. \n How do you want to pay for the order?","Payment method",JOptionPane.DEFAULT_OPTION,JOptionPane.INFORMATION_MESSAGE,null,plata,plata[0]);
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
                               p = JOptionPane.showOptionDialog(null,"Delivery type: Express mail (the order will be delivered in 24 hours). \n How do you want to pay for the order?","Payment method",JOptionPane.DEFAULT_OPTION,JOptionPane.INFORMATION_MESSAGE,null,plata,plata[0]);
                               
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
                            JOptionPane.showMessageDialog(null,"Are you sure you bought? Shopping cart is empty!","Empty shopping cart",JOptionPane.ERROR_MESSAGE);
                            
                    }
            }
        });
        sbc1.append("Reviews: \n\n");
        sbc1.append(" It's a wonderful book!\n\n");
        sbc1.append(" It helped me a lot.\n\n");
        sbc1.append(" Interesting book!\n\n");
        sbc1.append(" I recommend the book!\n\n");
        sbc1.append(" I liked the book!\n\n");
        b1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    input = JOptionPane.showInputDialog(sbc1.toString()+"Want to add a review?");
                        if(input != null)
                        {
                            sbc1.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Thanks for the review!","Reviews",JOptionPane.INFORMATION_MESSAGE);
                            
                        }
            }
        
        });
        sbc2.append("Reviews: \n\n");
        sbc2.append(" I really liked the book. I was always in suspense and tension.\n\n");
        sbc2.append(" A good and interesting book, with a captivating story.\n\n");
        sbc2.append(" Interesting book, worth reading!\n\n");
        sbc2.append(" Pretty addictive!\n\n");
        sbc2.append(" It's one of my favorite books!\n\n");
        b2.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    input = JOptionPane.showInputDialog(sbc2.toString()+"Want to add a review?");
                    if(input != null)
                    {
                            sbc2.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Thanks for the review!","Reviews",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        sbc3.append("Reviews: \n");
        sbc3.append(" I read it with my heart in my mouth!\n\n");
        sbc3.append(" Interesting topic.\n\n");
        sbc3.append(" Terrifying story!\n\n");
        sbc3.append(" Pretty addictive!\n\n");
        sbc3.append(" The best book written by Stephen King!\n\n");
        b3.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                     input = JOptionPane.showInputDialog(sbc3.toString()+"Want to add a review?");
                    if(input != null)
                    {
                            sbc3.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Thanks for the review!","Reviews",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        sbc4.append("Reviews: \n\n");
        sbc4.append(" An extraordinarily fantastic book !! \n Stephen King is one of the authors who never disappoints me. \n And Bill Hodges is a new favorite character of mine !!!\n\n");
        sbc4.append(" Mr. Mercedes has an opening that symbolizes the mastery of Stephen King's character.\n\n");
        sbc4.append(" I decided to read “Mr. Mercedes ”by Stephen King after a friend recommended it to me.\n\n");
        sbc4.append(" I made sure to choose a book by my favorite author as my first reading of the year and I do not regret the choice\n\n");
        sbc4.append(" MR. MERCEDES by STEPHEN KING was a fast-paced, fast-paced, action-packed detective \n mystery novel that sustained my interest from start to finish.\n\n");
        b4.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                     input = JOptionPane.showInputDialog(sbc4.toString()+"Want to add a review?");
                    if(input != null)
                    {
                            sbc4.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Thanks for the review!","Reviews",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        sbc5.append("Reviews: \n\n");
        sbc5.append(" Hayder does a fantastic job of developing her characters.\n\n");
        sbc5.append(" The Bird Man takes place at the dawn of the new millennium and follows the London Metropolitan Police murder team as they try to track down a possible serial killer Jack the Ripper. \n It's really fine!\n\n");
        sbc5.append(" I've been waiting for the right time to read Bird Man for years, and I finally made time last month - and this book was intense.\n\n");
        sbc5.append(" Wow. This book is very dark, twisted and captivating.\n\n");
        sbc5.append(" This book is a scary thriller, captivating from the first to the last page.\n\n");
        b5.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    input = JOptionPane.showInputDialog(sbc5.toString()+"Want to add a review?");
                    if(input != null)
                    {
                            sbc5.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Thanks for the review!","Reviews",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        sbc6.append("Reviews: \n\n");
        sbc6.append(" Well, it was great!\n\n");
        sbc6.append(" Melania is magnificent in 320 black cats. I woke up pleasantly surprised by her adventures and laughed heartily. She is definitely a captivating character.\n\n");
        sbc6.append(" Far too loud, I read and laugh with tears, I haven't read a book in a long time that would simply take me out of my daily life and give me an incredible state of well-being.\n\n");
        sbc6.append(" I must mention that the title of this novel intrigued me. It made me cringe and I wondered: what are 320 black cats all doing together?\n\n");
        sbc6.append(" The most successful novel of the series and anyway one of the first three best of the author. I don't even know if the 320 cats is a detective novel, or more of a parody.\n\n");
        b6.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    input = JOptionPane.showInputDialog(sbc6.toString()+"Want to add a review?");
                    if(input != null)
                    {
                            sbc6.append(" "+input+"\n\n");
                            JOptionPane.showMessageDialog(null,"Thanks for the review!","Reviews",JOptionPane.INFORMATION_MESSAGE);
                    }
            }
        
        });
        
    }
    
}
