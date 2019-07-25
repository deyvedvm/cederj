package br.edu.cederj.poo.classroom11;

import java.io.*;

public class CopyStringFile {

    public static void main(String[] args) {

        BufferedReader bufferedReader;
        BufferedWriter bufferedWriter;

        try {

            bufferedReader = new BufferedReader(new FileReader("src/resources/input.txt"));
            bufferedWriter = new BufferedWriter(new FileWriter("src/resources/output.txt"));

            String str;

            while ((str = bufferedReader.readLine()) != null) {
                bufferedWriter.write(str);
            }

            bufferedReader.close();
            bufferedWriter.close();

        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
}
