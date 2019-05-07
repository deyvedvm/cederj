package br.edu.cederj.poo.ap220182.questao1;

public class AP2_2018_2_Q1 {

    public static void main(String[] args) {

        Colecao colecao;
        colecao = new Vetor();

        String a = "A";
        String b = "B";
        String c = "C";

        colecao.adiciona(a);
        colecao.adiciona(b);
        colecao.adiciona(c);

        colecao.remove(b);

        colecao.lista();
    }
}
