package br.edu.cederj.poo.ad220192;

public class AD2_2019_2 {

    public static void main(String[] args) {

        Pasta p1 = new Pasta("dir1");
        p1.adiciona(new Arquivo("arquivo1.txt", 150));
        p1.adiciona(new Arquivo("arquivo2.txt", 200));

        Pasta p2 = new Pasta("dir2");
        p2.adiciona(new Arquivo("arquivo3.txt", 500));

        Pasta p3 = new Pasta("dir3");
        p3.adiciona(new Arquivo("arquivo4.txt", 350));
        p3.adiciona(p2);

        Pasta raiz = new Pasta("c:/");
        raiz.adiciona(p1);
        raiz.adiciona(p3);

        // Tive dúvida na remoção do item
        raiz.remove("dir1/arquivo1.txt");

        System.out.println(raiz.getTamanho());

        // Tive dúvida na indentação solicitada
        System.out.println(raiz);
    }
}
