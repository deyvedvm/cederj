package br.edu.cederj.poo.ad120181;

import java.time.LocalDate;
import java.time.Period;

class Video extends Midia {

    private String descricao;

    private int duracao;

    private int curtidas;

    Video(String autor, String titulo, String url, LocalDate dataPublicacao, String descricao, int duracao, int curtidas) {
        super(autor, titulo, url, dataPublicacao);
        this.descricao = descricao;
        this.duracao = duracao;
        this.curtidas = curtidas;
    }

    String retornaIdade() {

        LocalDate hoje = java.time.LocalDate.now();

        Period idade = java.time.Period.between(this.dataPublicacao, hoje);

        String sIdade = "";

        if (idade.getYears() > 0)
            sIdade += idade.getYears() + " anos ";

        if (idade.getMonths() > 0)
            sIdade += idade.getMonths() + " meses ";

        if (idade.getDays() > 0)
            sIdade += idade.getDays() + " dias";

        return sIdade;
    }

    public String toString() {

        return autor + " " + titulo + " " + retornaIdade();
    }
}
