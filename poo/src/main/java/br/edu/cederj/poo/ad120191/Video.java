package br.edu.cederj.poo.ad120191;

public class Video extends Midia {

    private String assunto;

    private String titulo;

    private String canal;

    private int visualizacoes;

    public Video(String assunto, String titulo, String canal, int visualizacoes, int duracao) {
        this.assunto = assunto;
        this.titulo = titulo;
        this.canal = canal;
        this.visualizacoes = visualizacoes;
        this.duracao = duracao;
    }

    public int getDuracao() {

        int duracaoTotal = this.duracao;

        if (this.visualizacoes > 1000 && this.visualizacoes < 10000) {
            duracaoTotal += this.duracao * 0.02;
        } else if (this.visualizacoes > 10000) {
            duracaoTotal += this.duracao * 0.05;
        }

        return duracaoTotal;
    }
}
