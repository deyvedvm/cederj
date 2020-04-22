package br.edu.cederj.poo.ap120191.questao2;

public class No {

    Figura figura;
    No proximo;

    public No(Figura figura) {
        this.figura = figura;
        this.proximo = null;
    }

    @Override
    public String toString() {
        return figura.toString();
    }
}
