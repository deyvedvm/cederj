package br.edu.cederj.poo.ap120191.questao2;

public class Quadrado extends Figura {

    private int lado;

    public Quadrado(int lado) {
        this.lado = lado;
    }

    @Override
    float calculaArea() {
        return lado * lado;
    }

    @Override
    public String toString() {
        return calculaArea() + "\tQ " + lado + "\n";
    }
}
