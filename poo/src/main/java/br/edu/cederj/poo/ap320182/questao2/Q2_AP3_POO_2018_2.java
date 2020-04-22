package br.edu.cederj.poo.ap320182.questao2;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Q2_AP3_POO_2018_2 {

    public static void main(String[] args) throws FileNotFoundException {
        int n, m;

        BufferedReader bufferedReader = new BufferedReader(new FileReader(args[0]));

        try {
            String str = bufferedReader.readLine();
            String[] strings;

            while (str != null) {
                strings = str.split(" ");
                n = Integer.parseInt(strings[0]);
                m = Integer.parseInt(strings[1]);

                if ((n == 0) && (m == 0)) {
                    System.out.println("Fim!");
                    bufferedReader.close();
                    return;
                }

                if ((n == 0) || (m == 0)) continue;

                if ((n < 2) || (m < 2) || (n > 100) || m > 100) continue;

                int matrix[][] = new int[n][m];
                int i, j;

                for (i = 0; i < n; i++) {
                    str = bufferedReader.readLine();
                    strings = str.split(" ");
                    for (j = 0; j < m; j++)
                        matrix[i][j] = Integer.parseInt(strings[j]);
                }

                int aux, carac1, carac2, carac3, carac4;
                carac1 = carac2 = carac3 = carac4 = 0;

                //carac1: Ninguém resolveu todos os problemas
                for (i = 0; i < n; i++) {
                    aux = 0;
                    for (j = 0; j < m; j++) aux += matrix[i][j];
                    if (aux == m) {
                        carac1 = 0;
                        break;
                    }
                }
                if (i == n) carac1 = 1;

                //carac2: O problema foi resolvido por pelo menos uma pessoa (não necessariamente a mesma)
                for (j = 0; j < m; j++) {
                    aux = 0;
                    for (i = 0; i < n; i++) aux += matrix[i][j];
                    if (aux == 0) {
                        carac2 = 0;
                        break;
                    }
                }
                if (j == m) carac2 = 1;

                //carac3: Não há nenhum problema resolvido por todos
                for (j = 0; j < m; j++) {
                    aux = 0;
                    for (i = 0; i < n; i++) aux += matrix[i][j];
                    if (aux == n) {
                        carac3 = 0;
                        break;
                    }
                }
                if (j == m) carac3 = 1;

                //carac4: Todos resolveram ao menos um problema //(não necessariamente o mesmo)
                for (i = 0; i < n; i++) {
                    aux = 0;
                    for (j = 0; j < m; j++) aux += matrix[i][j];
                    if (aux == 0) {
                        carac4 = 0;
                        break;
                    }
                }
                if (i == n) carac4 = 1;

                System.out.println(carac1 + carac2 + carac3 + carac4);
                str = bufferedReader.readLine();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
