package br.edu.cederj.poo.ap120171;

/**
 * Created by deyve on 07/05/17.
 */
public class Principal {

    private double valorTotal;

    Apto apto = new Apto(001, 2, 55, 150000);
    Carro carro = new Carro(001, "Fox", 2014, 37000);



    public void inventario(Apto apto){
        this.valorTotal += apto.preco;
    };

    public void inventario(Carro carro){
        this.valorTotal += carro.valor;
    }

    public static void main(String args[]){

    }

}
