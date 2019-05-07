package br.edu.cederj.poo.ap220182.questao1;

public class Vetor implements Colecao {

    private int tamanho;

    private Object[] elementos;

    Vetor() {
        elementos = new Object[1000];
        tamanho = 0;
    }

    @Override
    public void adiciona(Object elemento) {

        if (this.tamanho < this.elementos.length) {

            this.elementos[this.tamanho] = elemento;
            this.tamanho++;
        }
    }

    @Override
    public void remove(Object elemento) {

        for (int i = 0; i < this.elementos.length - 1; i++) {

            if (this.elementos[i] == elemento) {

                for (int j = i; j < this.elementos.length - 1; j++) {

                    this.elementos[i] = this.elementos[i + 1];
                }

                this.tamanho--;
            }
        }
    }

    @Override
    public void lista() {

        for (int i = 0; i < this.tamanho; i++) {
            System.out.println(elementos[i]);
        }
    }
}
