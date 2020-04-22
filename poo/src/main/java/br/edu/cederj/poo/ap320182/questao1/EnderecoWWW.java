package br.edu.cederj.poo.ap320182.questao1;

public class EnderecoWWW extends Recurso {

    public EnderecoWWW (String nome, String url) {
        super(nome, url);
    }

    @Override
    public boolean valido() {
        return this.url.startsWith("www");
    }
}
