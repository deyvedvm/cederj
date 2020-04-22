package br.edu.cederj.poo.ap320191.questao1;

import java.util.ArrayList;
import java.util.List;

public class Tarefas {

    List<Tarefa> tarefas;

    public Tarefas() {
        this.tarefas = new ArrayList<>();
    }

    public void adicionaTarefa(Tarefa tarefa) {
        tarefas.add(tarefa);
    }

    public void realizaTarefas() {
        tarefas.forEach(Tarefa::realizar);
    }

    public void imprimirTarefas() {
        tarefas.forEach(System.out::println);
    }
}
