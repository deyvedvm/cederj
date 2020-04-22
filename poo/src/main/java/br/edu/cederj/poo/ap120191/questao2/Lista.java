package br.edu.cederj.poo.ap120191.questao2;

public class Lista {

    No prim;

    public Lista() {
        this.prim = null;
    }

    void insere(Figura figura) {
        No novo = new No(figura);
        novo.proximo = prim;
        prim = novo;
    }

    public String toString() {
        String resp = "";
        No p = prim;

        while (p != null) {
            resp += p.toString();
            p = p.proximo;
        }

        return resp;
    }

}
