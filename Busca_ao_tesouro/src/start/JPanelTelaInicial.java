package start;

import java.awt.Dimension;
import java.awt.FlowLayout;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;

public class JPanelTelaInicial {

	private JPanel panel;
	private JLabel jlbImage;
	
	protected JPanelTelaInicial() {
		this.initializeJPanelTelaInicial();
	}
	
	private void initializeJPanelTelaInicial() {
		this.panel = new JPanel(new FlowLayout(FlowLayout.LEFT));
		this.panel.setPreferredSize(new Dimension(1200, 800));
		
		this.initializeConfigJPanel();
		
		this.panel.add(jlbImage);
	}
	
	private void initializeConfigJPanel() {
		this.jlbImage = new JLabel("");
		this.jlbImage.setHorizontalAlignment(SwingConstants.LEFT);
		this.jlbImage.setIcon(new ImageIcon("F:\\Github\\algoritmos_em_grafos\\busca-ao-tesouro\\Busca_ao_tesouro\\src\\image.png"));
		this.jlbImage.setBounds(0, 0, 750, 750);
//		this.jlbImage.setPreferredSize(new Dimension(750, 750));

	}
	
	protected JPanel getJPanel() {
		return this.panel;
	}
	
}
