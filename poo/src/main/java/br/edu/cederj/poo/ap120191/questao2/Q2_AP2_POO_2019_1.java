package br.edu.cederj.poo.ap120191.questao2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Q2_AP2_POO_2019_1 {

    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new FileReader(args[0]));

        try {
            Lista lista = new Lista();
            String str = bufferedReader.readLine();

            while (str != null) {
                String[] vs = str.split(" ");
                Figura figura;
                if (vs[0].equals("Q")) {
                    figura = new Quadrado(Integer.parseInt(vs[1]));
                } else if (vs[0].equals("R")) {
                    figura = new Retangulo(Integer.parseInt(vs[1]), Integer.parseInt(vs[2]));
                } else {
                    figura = new Triangulo(Integer.parseInt(vs[1]), Integer.parseInt(vs[2]));
                }

                lista.insere(figura);
                str = bufferedReader.readLine();
            }

            bufferedReader.close();
            Ordaena(lista);
            System.out.println(lista);
        } catch (Exception e) {
            System.out.println("Excecao\n");
        }
    }

    static void Ordaena(Lista lista) {
        for (No p = lista.prim; p != null; p = p.proximo) {
            No menor = p;

            for (No q = p.proximo; q != null; q = q.proximo)
                if (menor.figura.calculaArea() > q.figura.calculaArea()) menor = q;

            if (menor != p) {
                Figura temp = menor.figura;
                menor.figura = p.figura;
                p.figura = temp;
            }
        }
    }
}
