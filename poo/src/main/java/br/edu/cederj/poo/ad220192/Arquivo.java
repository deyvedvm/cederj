package br.edu.cederj.poo.ad220192;

public class Arquivo extends Item {

    private int tamanho;

    public Arquivo(String nome, int tamanho) {
        this.nome = nome;
        this.tamanho = tamanho;
    }

    public int getTamanho() {
        return this.tamanho;
    }

    @Override
    public String toString() {
        return this.nome + "\n\t";
    }
}
