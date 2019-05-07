package br.edu.cederj.poo.ap220182.questao3;

public class No {

    int valor, ocorr;
    No prox;

    public No(int valor) {

        this.valor = valor;
        ocorr = 1;
        this.prox = null;
    }

    public String toString() {
        return valor + " (" + ocorr + ")";
    }
}
