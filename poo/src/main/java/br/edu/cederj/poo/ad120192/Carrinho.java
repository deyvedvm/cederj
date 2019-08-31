package br.edu.cederj.poo.ad120192;

import java.util.Arrays;

/**
 * Carrinho
 */
public class Carrinho {

    private Cliente cliente;

    private IProduto[] produtos;

    private Double total;

    public Carrinho(Cliente cliente, IProduto[] produtos) {
        this.cliente = cliente;
        this.produtos = produtos;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public IProduto[] getProdutos() {
        return produtos;
    }

    public Double getTotal() {

        total = 0.0;

        for (IProduto produto : produtos) {
            total += produto.getPreco();
        }

        return total;
    }

    @Override
    public String toString() {
        return String.format("Carrinho: {cliente=%s, produtos=%s, total=%s}", cliente, Arrays.toString(produtos), total);
    }
}
