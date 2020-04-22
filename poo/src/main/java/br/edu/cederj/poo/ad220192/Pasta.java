package br.edu.cederj.poo.ad220192;

import java.util.ArrayList;
import java.util.List;

public class Pasta extends Item {

    private List<Item> conteudo = new ArrayList<>();

    public Pasta(String nome) {
        this.nome = nome;
    }

    public void adiciona(Item item) {
        this.conteudo.add(item);
    }

    public void remove(String nome) {
        String[] strings = nome.split("/");

        for (Item item : conteudo) {
            if (item.nome.equals(strings[1])) {
                this.conteudo.remove(item);
            }
        }
    }

    public int getTamanho() {

        int tamanho = 0;

        for (Item item : this.conteudo) {
            tamanho += item.getTamanho();
        }

        return tamanho;
    }

    @Override
    public String toString() {
        return this.nome + "\n\t" + conteudo;
    }
}
