package br.edu.cederj.poo.ap320191.questao1;

import java.time.LocalDate;

public class Recorrente extends Tarefa {

    enum Frequencia {DIARIA, SEMANAL, MENSAL}

    LocalDate dia;
    Frequencia frequencia;

    public Recorrente(String descricao, LocalDate dia, Frequencia frequencia) {
        super(descricao);
        this.dia = dia;
        this.frequencia = frequencia;
    }

    public void realizar() {
        switch (this.frequencia) {
            case DIARIA:
                this.dia = this.dia.plusDays(1);
                break;
            case SEMANAL:
                this.dia = this.dia.plusWeeks(1);
                break;
            case MENSAL:
                this.dia = this.dia.plusMonths(1);
                break;
        }
    }
}
