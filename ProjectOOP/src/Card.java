import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.time.LocalDate;
import java.util.*;
import javax.swing.*;
public class Card extends JFrame{
    private JButton btn;
    private JComboBox box1;
    private JTextField txt1,txt2,txt3;
    private String[] tip={"Visa","MasterCard","Maestro"};
    private int anScris;
    private int anCurent;
    private LocalDate dataCurenta;
    private int lunaCurenta;
    private int lunaScrisa;
    public Card(){
        this.setTitle("Plata cu cardul");
        this.setLayout(new GridLayout(5,2,10,10));
        
        this.add(new JLabel("Tipul cartii: "));
        box1= new JComboBox(tip);
        add(box1);
        this.add(new JLabel("Numarul cartii (Te rog sa introduci ultimele 4 numere): "));
        txt1=new JTextField(16);
        add(txt1);
        
        this.add(new JLabel("Data: Luna (Te rog scrie luna in cifre (1-12): "));
        txt2= new JTextField(5);
        add(txt2);
        this.add(new JLabel("Anul (Te rog scrie anul de forma yy): "));
        txt3= new JTextField(5);
        add(txt3);
        
        btn=new JButton("Plateste");
        add(btn);
        
        setSize(800,250);
        setLocationRelativeTo(null);
        setVisible(true);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                    
         btn.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    dataCurenta= LocalDate.now();
                    anScris = Integer.parseInt(txt3.getText());
                    anCurent = (dataCurenta.getYear())%100;
                    
                    if(txt1.getText().equals("") || txt2.getText().equals("") || txt3.getText().equals(""))
                        JOptionPane.showMessageDialog(null,"Trebuie sa introduci toate datele!","Date invalide",JOptionPane.ERROR_MESSAGE);
                    else
                    {
                    if(anCurent<anScris)
                    {
                       
                        JOptionPane.showMessageDialog(null, "Plata finalizata!");
                    }
                    else
                    {
                        if(anCurent>anScris)
                            JOptionPane.showMessageDialog(null,"Cardul nu este valid!","Eroare",JOptionPane.ERROR_MESSAGE);
                        else
                        {
                            if(anCurent==anScris)
                            {
                                lunaCurenta = dataCurenta.getMonthValue();
                                lunaScrisa = Integer.parseInt(txt2.getText());
                                
                                if(lunaCurenta>=lunaScrisa)
                                    JOptionPane.showMessageDialog(null,"Cardul nu este valid!","Eroare",JOptionPane.ERROR_MESSAGE);
                                else
                                {
                                    if(lunaCurenta<lunaScrisa)
                                        JOptionPane.showMessageDialog(null, "Plata finalizata!");
                                }      
                                
                            }
                        }
                    }
                    }
                    
            }

        });
    }
}
