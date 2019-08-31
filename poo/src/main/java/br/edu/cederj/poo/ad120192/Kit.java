package br.edu.cederj.poo.ad120192;

import java.util.Arrays;

/**
 * Kit
 */
public class Kit implements IProduto {

    private Produto[] produto;

    private ProdutoComposto[] produtoComposto;

    public Kit(Produto[] produto, ProdutoComposto[] produtoComposto) {
        this.produto = produto;
        this.produtoComposto = produtoComposto;
    }

    public Produto[] getProduto() {
        return produto;
    }

    public ProdutoComposto[] getProdutoComposto() {
        return produtoComposto;
    }

    public Double getPreco() {

        double preco = 0.0;

        for (Produto produto : produto) {
            preco += produto.getPreco();
        }

        for (ProdutoComposto produtoComposto : produtoComposto) {
            preco += produtoComposto.getPreco();
        }

        return preco;
    }

    @Override
    public String toString() {
        return String.format("Kit: {produto=%s, produtoComposto=%s}", Arrays.toString(produto), Arrays.toString(produtoComposto));
    }
}
