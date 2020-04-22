package br.edu.cederj.poo.ap320182.questao1;

public class Imagem extends Recurso {
    int tamanho;

    public Imagem(String nome, String url, int tamanho) {
        super(nome, url);
        this.tamanho = tamanho;
    }

    @Override
    public boolean valido() {
        return this.url.endsWith("jpg") || this.url.endsWith("png");
    }
}
