package br.edu.cederj.poo.ap120182.questao2;

public class Main {

    public static void main(String[] args) {

        Reuniao socios = new Reuniao("Reunião com sócios", 15, 17, 13, 8, 2018);
        Reuniao clientes = new Reuniao("Reunião com clientes", 17, 18, 13, 8, 2018);
        Reuniao confraternizacao = new Reuniao("Confraternização", 21, 23, 13, 8, 2018);

        Reuniao[] reunioes = {socios, clientes, confraternizacao};

        int duracao = 0;

        for (Reuniao reuniao : reunioes) {

            duracao += reuniao.getDuracao();
        }

        System.out.println("O tempo total de reunião é: " + duracao + " horas");
    }
}
