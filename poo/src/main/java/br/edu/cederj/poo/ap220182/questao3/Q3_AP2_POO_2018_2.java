package br.edu.cederj.poo.ap220182.questao3;

import java.io.*;

public class Q3_AP2_POO_2018_2 {

    public static void main(String[] args) throws IOException {

        BufferedReader in;
        in = new BufferedReader(new FileReader(args[0]));
        BufferedWriter out;
        out = new BufferedWriter(new FileWriter("saida-" + args[0]));
        try {
            Lista l = new Lista();
            String s = in.readLine();
            while (s != null) {
                l.insere(Integer.parseInt(s));
                s = in.readLine();
            }
            in.close();
            Ordena(l);
            out.write(l.toString());
            out.close();
        } catch (Exception e) {
            System.out.println("Excecao\n");
        }
    }

    static void Ordena(Lista l) {
        for (No p = l.prim; p != null; p = p.prox) {
            No maior = p;
            for (No q = p.prox; q != null; q = q.prox)
                if ((maior.ocorr < q.ocorr) || ((maior.ocorr == q.ocorr) &&
                        (maior.valor > q.valor))) maior = q;
            if (maior != p) {
                int temp = maior.valor;
                maior.valor = p.valor;
                p.valor = temp;
                temp = maior.ocorr;
                maior.ocorr = p.ocorr;
                p.ocorr = temp;
            }
        }
    }
}

