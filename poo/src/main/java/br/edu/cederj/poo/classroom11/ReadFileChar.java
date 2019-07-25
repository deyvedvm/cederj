package br.edu.cederj.poo.classroom11;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

public class ReadFileChar {

    public static void main(String[] args) {

        InputStream inputStream = null;

        int index = -1;

        try {
            inputStream = new FileInputStream("src/resources/data.txt");

        } catch (FileNotFoundException nfe) {
            System.out.println("File Not Found");
            System.exit(0);
        }

        do {

            try {

                index = inputStream.read();

            } catch (IOException ioe) {

                System.out.println("The file cannot be read");
            }

            if (index != -1) {
                System.out.println((char) index);
            }

        } while (index != -1);

    }

}
