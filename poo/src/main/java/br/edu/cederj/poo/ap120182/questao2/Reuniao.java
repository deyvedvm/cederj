package br.edu.cederj.poo.ap120182.questao2;

import br.edu.cederj.poo.ap120182.questao1.Data;

public class Reuniao extends Data {

    String assunto;

    int horaInicio;

    int horaFim;

    public Reuniao(String assunto, int horaInicio, int horaFim, int dia, int mes, int ano) {
        super(dia, mes, ano);
        this.assunto = assunto;
        this.horaInicio = horaInicio;
        this.horaFim = horaFim;
    }

    public int getDuracao() {
        return this.horaFim - this.horaInicio;
    }
}
