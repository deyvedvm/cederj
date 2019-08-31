package br.edu.cederj.poo.ad120192;

public class Main {

    public static void main(String[] args) {

        Cliente deyve = new Cliente("Deyve");

        Produto pincel = new Produto(1, "Pincel", 6.00);
        Produto rolo = new Produto(2, "Rolo", 4.50);
        Produto lixa = new Produto(3, "Lixa", 3.00);
        Produto bandeja = new Produto(4, "Bandeja.", 3.00);

        System.out.println(bandeja);

        Produto[] produtos = {pincel, bandeja};


        ProdutoComposto produtoComposto = new ProdutoComposto(produtos);

        System.out.println(produtoComposto);

        ProdutoComposto[] produtosCompostos = {produtoComposto};


        Kit kit = new Kit(produtos, produtosCompostos);

        System.out.println(kit);

        Kit[] kits = {kit};

        Carrinho carrinho = new Carrinho(deyve, kits);

        System.out.println(carrinho);

    }

}
