package br.edu.cederj.poo.ap120191.questao1;

public class Entrada {

    private final String palavaOrigem;
    private final String palavraTraducao;
    private final String idiomaOrigem;
    private final String idiomaTraducao;

    public Entrada(String palavaOrigem, String palavraTraducao, String idiomaOrigem, String idiomaTraducao) {
        this.palavaOrigem = palavaOrigem;
        this.palavraTraducao = palavraTraducao;
        this.idiomaOrigem = idiomaOrigem;
        this.idiomaTraducao = idiomaTraducao;
    }

    public String getPalavaOrigem() {
        return palavaOrigem;
    }

    public String getPalavraTraducao() {
        return palavraTraducao;
    }

    public String getIdiomaOrigem() {
        return idiomaOrigem;
    }

    public String getIdiomaTraducao() {
        return idiomaTraducao;
    }
}
