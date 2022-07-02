import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class ContBancar extends JFrame{
    private JTextField txt1,txt2;
    private JButton btn1;
    private String numar;
    public ContBancar(){
        this.setTitle("Payment by card");
        this.setLayout(new GridLayout(3,2,10,10));
        
        this.add(new JLabel("Bank name: "));
        txt1=new JTextField(16);
        add(txt1);
        
        this.add(new JLabel("The account number: "));
        txt2= new JTextField(5);
        add(txt2);
        
        btn1=new JButton("Checkout");
        add(btn1);
        
        setSize(250,150);
        setLocationRelativeTo(null);
        setVisible(true);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        
         btn1.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                    numar=txt2.getText();
                    if(txt1.getText().equals("") || txt2.getText().equals(""))
                        JOptionPane.showMessageDialog(null,"You must enter all the data!","Invalid data",JOptionPane.ERROR_MESSAGE);
                    else
                    {
                    if(numar.length()==16)
                    {  
                        JOptionPane.showMessageDialog(null, "Payment completed! ");
                       
                     }
                            
                    else
                        JOptionPane.showMessageDialog(null, "Enter the data correctly!");
                    }
            }    
        });
    }
}
