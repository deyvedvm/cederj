package br.edu.cederj.poo.ap320182.questao1;

public abstract class Recurso {
    String nome;
    String url;

    public Recurso(String nome, String url) {
        this.nome = nome;
        this.url = url;
    }

    public String toString() {
        return this.url;
    }

    public abstract boolean valido();
}
