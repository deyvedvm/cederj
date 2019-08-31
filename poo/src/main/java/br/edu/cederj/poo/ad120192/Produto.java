package br.edu.cederj.poo.ad120192;

/**
 * Produto
 */
public class Produto implements IProduto {

    private Integer codigo;

    private String nome;

    private Double preco;

    public Produto(Integer codigo, String nome, Double preco) {
        this.codigo = codigo;
        this.nome = nome;
        this.preco = preco;
    }

    public Integer getCodigo() {
        return codigo;
    }

    public String getNome() {
        return nome;
    }

    public Double getPreco() {
        return preco;
    }

    @Override
    public String toString() {
        return String.format("Produto: {codigo=%d, nome='%s', preco=%s}", codigo, nome, preco);
    }
}
