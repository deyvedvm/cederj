package br.edu.cederj.poo.ap120191.questao2;

public class Triangulo extends Figura {

    private int base, altura;

    public Triangulo(int base, int altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    float calculaArea() {
        return (base * altura) / 2.0f;
    }

    public String toString() {
        return calculaArea() + "\tT " + base + " " + altura + "\n";
    }
}
