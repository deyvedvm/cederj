package br.edu.cederj.poo.ap320191.questao1;

public class Tarefa {
    String descricao;
    boolean feita;

    public Tarefa(String descricao) {
        this.descricao = descricao;
        this.feita = false;
    }

    public void realizar() {
        this.feita = true;
    }

    @Override
    public String toString() {
        return "Tarefa: " + this.descricao + " - " + (this.feita ? "feita" : "não feita");
    }
}
