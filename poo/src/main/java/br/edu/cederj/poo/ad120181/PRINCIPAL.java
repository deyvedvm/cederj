package br.edu.cederj.poo.ad120181;

import java.time.LocalDate;

public class PRINCIPAL {

    public static void main(String[] args) {

        Video video1 = new Video("Loiane Groner",
                "Curso Angular #01: Introdução",
                "https://www.youtube.com/watch?v=tPOMG0D57S0&t=1s",
                LocalDate.of(2016, 7, 5),
                "Curso de Angular Gratuito e Completo com Certificado",
                998,
                7200);

        Ebook ebook = new Ebook("Marijn Haverbeke",
                "Eloquent JavaScript",
                "http://eloquentjavascript.net/3rd_edition/",
                LocalDate.of(2017, 3, 6),
                472);

        Midia midias[] = {video1, ebook};

        for (Midia midia : midias) {

            System.out.println(midia);
        }
    }
}

