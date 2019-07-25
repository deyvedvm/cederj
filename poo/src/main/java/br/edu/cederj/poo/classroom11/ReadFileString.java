package br.edu.cederj.poo.classroom11;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFileString {

    public static void main(String[] args) {

        BufferedReader bufferedReader;

        try {

            bufferedReader = new BufferedReader(new FileReader("src/resources/data.txt"));

            String str;

            while ((str = bufferedReader.readLine()) != null) {
                System.out.println(str);
            }

            bufferedReader.close();

        } catch (IOException ioe) {
            System.out.println("Error reading file");
        }

    }

}
