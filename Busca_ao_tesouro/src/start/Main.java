package start;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.BorderLayout;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import javax.swing.SwingConstants;

public class Main {

	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Main window = new Main();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Main() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setTitle("Busca ao Tesouro");
		frame.setBounds(100, 100, 1000, 800);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setLocationRelativeTo(null);
		
		
		JPanelTelaInicial start = new JPanelTelaInicial();
		frame.getContentPane().add(start.getJPanel());
		
//		JPanel panel = new JPanel();
//		panel.setBounds(0, 11, 1200, 10);
//		frame.getContentPane().add(panel);
//		
//		JLabel lblNewLabel = new JLabel("");
//		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
//		lblNewLabel.setIcon(new ImageIcon("F:\\Github\\algoritmos_em_grafos\\busca-ao-tesouro\\Busca_ao_tesouro\\src\\image.png"));
//		panel.add(lblNewLabel);
//		
		frame.setVisible(true);
		
		
	}
}
