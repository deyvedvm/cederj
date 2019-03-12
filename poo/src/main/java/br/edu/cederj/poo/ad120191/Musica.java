package br.edu.cederj.poo.ad120191;

public class Musica extends Midia {

    private String nome;

    private String compositor;

    private String interprete;

    public Musica(String nome, String compositor, String interprete, Integer duracao) {
        this.nome = nome;
        this.compositor = compositor;
        this.interprete = interprete;
        this.duracao = duracao;
    }

    public int getDuracao() {
        return duracao;
    }
}
