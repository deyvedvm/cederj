package br.edu.cederj.poo.ap220182.questao3;

public class Lista {

    No prim;

    Lista() {
        prim = null;
    }

    void insere(int valor) {

        No novo = busca(valor);
        if (novo == null) {
            novo = new No(valor);
            novo.prox = prim;
            prim = novo;
        } else novo.ocorr++;
    }

    No busca(int valor) {

        No p = prim;
        while ((p != null) && (p.valor != valor)) p = p.prox;
        return p;
    }


    public String toString() {

        String resp = "";
        No p = prim;
        while (p != null) {
            resp = resp + p.toString() + "\n";
            p = p.prox;
        }
        return resp;
    }

}