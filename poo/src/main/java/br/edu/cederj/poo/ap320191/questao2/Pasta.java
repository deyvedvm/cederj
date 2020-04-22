package br.edu.cederj.poo.ap320191.questao2;

import java.util.ArrayList;
import java.util.List;

public class Pasta extends Elemento {
    private List<Elemento> elementos = new ArrayList<>();

    public Pasta(String nome) {
        super(nome);
    }

    public void add(Elemento elemento) {
        elementos.add(elemento);
    }

    @Override
    public int getTamanho() {
        int total = 0;

        for (Elemento elemento : elementos) {
            total += elemento.getTamanho();
        }

        return total;
    }
}
