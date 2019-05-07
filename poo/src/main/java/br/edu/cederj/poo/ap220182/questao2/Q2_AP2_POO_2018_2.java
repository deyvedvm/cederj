package br.edu.cederj.poo.ap220182.questao2;

import java.io.*;

public class Q2_AP2_POO_2018_2 {

    public static void main(String[] args) throws IOException {

        int numeroDeArquivos = Integer.parseInt(args[0]), i;

        if (numeroDeArquivos <= 0) return;

        String[] nomesDosArquivos = new String[numeroDeArquivos];

        for (i = 1; i <= numeroDeArquivos; i++) {

            nomesDosArquivos[i - 1] = args[i];
        }

        Merge(numeroDeArquivos, nomesDosArquivos, args[numeroDeArquivos + 1]);
    }

    static void Merge(int numeroDeArquivos, String[] nomeDosArquivos, String arquivoDeSaida) throws IOException {

        BufferedReader[] bufferedReaders = new BufferedReader[numeroDeArquivos];

        for (int i = 0; i < numeroDeArquivos; i++) {

            bufferedReaders[i] = new BufferedReader(new FileReader(nomeDosArquivos[i]));
        }

        BufferedWriter bufferedWriter;
        bufferedWriter = new BufferedWriter(new FileWriter(arquivoDeSaida));

        String resp = "", s;

        int[] vet = new int[numeroDeArquivos];

        try {

            for (int i = 0; i < numeroDeArquivos; i++) {
                s = bufferedReaders[i].readLine();
                if (s != null) vet[i] = Integer.parseInt(s);
                else vet[i] = Integer.MAX_VALUE;
            }

            int ind = menorInd(vet);

            while (ind != Integer.MAX_VALUE) {
                resp = resp + vet[ind] + "\n";
                s = bufferedReaders[ind].readLine();
                if (s != null) vet[ind] = Integer.parseInt(s);
                else vet[ind] = Integer.MAX_VALUE;
                ind = menorInd(vet);
            }
            for (int i = 0; i < numeroDeArquivos; i++) bufferedReaders[i].close();
            bufferedWriter.write(resp);
            bufferedWriter.close();

        } catch (Exception e) {

            System.out.println("Excecao\n");
        }
    }

    static int menorInd(int[] vet) {

        int resp = Integer.MAX_VALUE, menor = Integer.MAX_VALUE;

        for (int i = 0; i < vet.length; i++)
            if (menor > vet[i]) {
                menor = vet[i];
                resp = i;
            }
        return resp;
    }
}
