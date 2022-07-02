import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class Register extends JFrame{
    private String[] nr={"0","1","2","3","4","5","6","7","8","9"};
    private String[] caractere={"@","!",".","_","-","/"};
    private  JTextField t3,t4,t5,t6,t7,t8,t9;
    private JButton b3;
    public static String username,parola;
    private FileWriter file;
    private String nume, prenume;
    private String s, s1, s2, s3, s4, A;
    private int m, l;
    public Register(){
        this.setTitle("Register");
        this.setLayout(new GridLayout(9,2,10,10));
        this.add(new JLabel(""));
        t3=new JTextField(10);
        add(t3);
        
        this.add(new JLabel("Surname"));
        t5=new JTextField(10);
        add(t5);
        
        
        this.add(new JLabel(" Postal address: Street: "));
        t4=new JTextField();
        add(t4);
        this.add(new JLabel(" Block: "));
        t6=new JTextField();
        add(t6);
        this.add(new JLabel(" Apartment: "));
        t8=new JTextField();
        add(t8);
        this.add(new JLabel(" Postal code: "));
        t9=new JTextField();
        add(t9);
        
        
        b3=new JButton("Login");
        add(b3);
       
        JOptionPane.showMessageDialog(null,"If you do not have anything to enter when entering the data, please write \'-\'");
        
        setSize(600,350);
        setLocationRelativeTo(null);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        b3.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
              if(t3.getText().equals("") || t4.getText().equals("") || t5.getText().equals("")|| t6.getText().equals("")|| t8.getText().equals("")|| t9.getText().equals(""))
                  JOptionPane.showMessageDialog(null,"You must enter all the data!","Invalid data",JOptionPane.ERROR_MESSAGE);
              else
              { 
                  if(t9.getText().length() == 6){
                  
                    nume=t5.getText();
                    prenume=t3.getText();

              
                    m=(int)(Math.random()*nr.length);
                    //username
                    s=prenume;
                    s1=nr[m];
              
                    m=(int)(Math.random()*nr.length);
                    s2=nr[m];
              
                    m=(int)(Math.random()*nr.length);
                    s3=nr[m];
              
                    username=s+s1+s2+s3;
              
                    //parola
                    A=nume;
                    l=(int)(Math.random()*caractere.length);
                    s1=caractere[l];
              
                    l=(int)(Math.random()*caractere.length);
                    s2=caractere[l];
              
                    l=(int)(Math.random()*caractere.length);
                    s3=caractere[l];
                    l=(int)(Math.random()*caractere.length);
                    s4=caractere[l];
              
                    parola=s1+A+s2+s3+s4;
              
                    JOptionPane.showMessageDialog(null,"Username: "+ username+"\n"+"Parola: "+parola);
                    new Bookstore();
                    dispose();
                 
                    try{
                        file = new FileWriter("continregistrare.txt");
                        file.write(username+"\n"+parola);
                        file.close();
                    } catch (IOException a){
                                a.printStackTrace();
                            }
                    
                    }
                    
                    else
                        JOptionPane.showMessageDialog(null,"Try to enter the data correctly!","Invalid data",JOptionPane.ERROR_MESSAGE);
              }
              
    }
            });
}
}
        
    
  
