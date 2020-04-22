package br.edu.cederj.poo.ap320182.questao1;

import java.util.ArrayList;
import java.util.List;

public class AP3_2018_2_Q1 {

    public static void main(String[] args) {

        //Nome e url
        EnderecoWWW e = new EnderecoWWW("Cederj", "www.cederj.edu.br");

        //Nome, url e tamanho da imagem
        Imagem i = new Imagem("Cederj", "http://cederj.edu.br/fundacao/wp-content/uploads/2014/03/marca_fundacao_cecierj_consorcio_cederj.png", 25);

        List<Recurso> pagina = new ArrayList<>();
        pagina.add(e);
        pagina.add(i);

        for (Recurso r : pagina)
            System.out.println("O recurso " + r.toString() + " eh " + r.valido());
    }
}
