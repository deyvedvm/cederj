package br.edu.cederj.poo.ap120191.questao1;

public class AP2_2019_1_Q1 {

    public static void main(String[] args) {
        Tradutor dic = new Tradutor();
        dic.adiciona(new Entrada("carro", "car", "pt", "en"));
        dic.adiciona(new Entrada("table", "mesa", "en", "pt"));
        dic.adiciona(new Entrada("voiture", "carro", "fr", "pt"));
        dic.adiciona(new Entrada("dog", "cachorro", "en", "pt"));
        dic.adiciona(new Entrada("pao", "pane", "pt", "it"));
        System.out.println(dic.geraEntradas("pt", "en"));
    }
}
