package application;

import java.util.ArrayList;
import java.util.Collections;

public class Questao3 {

	public static void main(String args[]) {
		ArrayList<String> lista = new ArrayList<>();
		lista.add("VERDE");
		lista.add("AZUL");
		lista.add("VERMELHO");
		lista.add("AMARELO");
		lista.add("CINZA");
		// Insira na linha imediatamente a seguir a linha de código que atenda ao requisito
		lista.remove(2);

		System.out.println("Lista após exclusão: " + lista);
		// Insira na linha imediatamente a seguir a linha de código que atenda ao requisito
		Collections.sort(lista);

		System.out.println("Lista após da ordenação: " + lista);
		alterar(lista, 2, "BRANCO");
	}
	// A partir da próxima linha, crie o método alterar(lista, indice, novaCor).
	public static void alterar(ArrayList<String> lista, int ind, String cor) {
		lista.remove(ind);
		lista.add(ind, cor);
		System.out.println("Lista após a atualização: " + lista);
	}

}
