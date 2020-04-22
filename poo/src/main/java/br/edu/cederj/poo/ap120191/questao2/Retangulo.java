package br.edu.cederj.poo.ap120191.questao2;

public class Retangulo extends Figura {

    private int comprimento, altura;

    public Retangulo(int comprimento, int altura) {
        this.comprimento = comprimento;
        this.altura = altura;
    }

    @Override
    float calculaArea() {
        return comprimento * altura;
    }

    @Override
    public String toString() {
        return calculaArea() + "\tR " + comprimento + " " + altura + "\n";
    }
}
