package MasinaTuring;
public class Tranzitie {

	private String stareInitiala;
	private char simbolInitial;
	private String stareFinala;
	private char simbolFinal;
	private char directie;

	public Tranzitie(String stareInitiala, char simbolInitial, String stareFinala, char simbolFinal,char directie) {
		this.stareInitiala = stareInitiala;
		this.simbolInitial = simbolInitial;
		this.stareFinala = stareFinala;
		this.simbolFinal = simbolFinal;
		this.directie = directie;
	}

	public String getStareInitiala() {
		return stareInitiala;
	}


	public void setStareInitiala(String stareInitiala) {
		this.stareInitiala = stareInitiala;
	}


	public char getSimbolInitial() {
		return simbolInitial;
	}


	public void setSimbolInitial(char simbolInitial) {
		this.simbolInitial = simbolInitial;
	}


	public String getStareFinala() {
		return stareFinala;
	}


	public void setStareFinala(String stareFinala) {
		this.stareFinala = stareFinala;
	}


	public char getSimbolFinal() {
		return simbolFinal;
	}


	public void setSimbolFinal(char simbolFinal) {
		this.simbolFinal = simbolFinal;
	}


	public char getDirectie() {
		return directie;
	}


	public void setDirectie(char directie) {
		this.directie = directie;
	}
	
}