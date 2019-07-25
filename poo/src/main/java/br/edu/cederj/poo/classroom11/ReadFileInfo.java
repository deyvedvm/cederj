package br.edu.cederj.poo.classroom11;

import java.io.File;

public class ReadFileInfo {

    public static void main(String[] args) {

        File file = new File("src/resources/data.txt");

        if (file.exists()) {
            System.out.println("Absolute Path: " + file.getAbsolutePath());
            System.out.println("File length: " + file.length() + " bytes");
            System.out.println("Can Write?: " + (file.canWrite() ? "Yes" : "No"));
        }
    }
}
