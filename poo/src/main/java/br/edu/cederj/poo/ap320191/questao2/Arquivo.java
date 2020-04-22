package br.edu.cederj.poo.ap320191.questao2;

public class Arquivo extends Elemento {
    private int tamanho;

    public Arquivo(String nome, int tamanho) {
        super(nome);
        this.tamanho = tamanho;
    }

    @Override
    public int getTamanho() {
        return this.tamanho;
    }
}
