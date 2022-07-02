import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.util.*;

public  class Bookstore extends JFrame {
    private JTextField t1;
    private JPasswordField t2;
    private JButton b1,b2;
    private BufferedReader reader;
    public Bookstore(){
        this.setTitle("Bun venit!");
         this.setLayout(new GridLayout(3,2,10,10));
        
         this.add(new JLabel("Username"));
        t1=new JTextField(10);
        add(t1);
        
         this.add(new JLabel("Parola"));
        t2=new JPasswordField(15);
        add(t2);
        
        b1=new JButton("Login");
        add(b1);
        b2=new JButton("Sign up");
        add(b2);
        setSize(250,150);
        setLocationRelativeTo(null);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        b1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                
                try{
                    reader = new BufferedReader(new FileReader("continregistrare.txt"));
                    String line = reader.readLine();
                    String line2 = reader.readLine();
                    if(line != null && line2 !=null)
                    {
                       if((t1.getText().equals(Register.username)&&t2.getText().equals(Register.parola)) || (line.equals(t1.getText()) && line2.equals(t2.getText())))
                            {       
                                JOptionPane.showMessageDialog(null,"Te-ai logat!","login",JOptionPane.INFORMATION_MESSAGE);
                                dispose();  
                                 new ListaCarti();
                            }
                     
                        else
                            {
                                JOptionPane.showMessageDialog(null, "Nu sunteti abonat!");
                            } 
                    }
                }catch (IOException a){
                    a.printStackTrace();
                }
                     
            }
        });
        
         b2.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    dispose();   
                    new Register();
            }

           

            
        });
        
    }
    
    public static void main(String[] args) {
       JFrame f = new Bookstore();
      
    }

    
}
