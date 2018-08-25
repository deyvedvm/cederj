package br.edu.cederj.poo.ad120181;

import java.time.LocalDate;

class Midia {

    protected String autor;

    protected String titulo;

    private String url;

    protected LocalDate dataPublicacao;

    Midia(String autor, String titulo, String url, LocalDate dataPublicacao) {
        this.autor = autor;
        this.titulo = titulo;
        this.url = url;
        this.dataPublicacao = dataPublicacao;
    }

    @Override
    public String toString() {
        return autor + " " + titulo + " " + dataPublicacao;
    }
}
