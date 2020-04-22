package br.edu.cederj.poo.ap320191.questao2;

public abstract class Elemento {
    private String nome;

    public Elemento(String nome) {
        this.nome = nome;
    }

    public abstract int getTamanho();
}
