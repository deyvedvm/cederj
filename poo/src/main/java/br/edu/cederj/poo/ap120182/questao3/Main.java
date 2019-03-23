package br.edu.cederj.poo.ap120182.questao3;

import java.util.Scanner;

class Elemento {

    int numero, resto;

    Elemento(int n, int r) {
        numero = n;
        resto = r;
    }

    public String toString() {
        return numero + "";
    }
}

public class Main {

    Scanner scanner = new Scanner(System.in);

    int n = scanner.nextInt(), m = scanner.nextInt();

}
