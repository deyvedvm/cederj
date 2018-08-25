package br.edu.cederj.poo.ad120181;

import java.time.LocalDate;

class Ebook extends Midia {

    private int paginas;

    Ebook(String autor, String titulo, String url, LocalDate dataPublicacao, int paginas) {
        super(autor, titulo, url, dataPublicacao);
        this.paginas = paginas;
    }
}
