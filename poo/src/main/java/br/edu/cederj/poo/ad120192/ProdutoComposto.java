package br.edu.cederj.poo.ad120192;

import java.util.Arrays;

/**
 * Produto Composto
 */
public class ProdutoComposto implements IProduto {

    private Produto[] produtos;

    public ProdutoComposto(Produto[] produtos) {
        this.produtos = produtos;
    }

    public Double getPreco() {

        double preco = 0.0;

        for (Produto produto : produtos) {
            preco += produto.getPreco();
        }

        return preco;
    }

    @Override
    public String toString() {
        return String.format("ProdutoComposto: {produtos=%s}", Arrays.toString(produtos));
    }
}
