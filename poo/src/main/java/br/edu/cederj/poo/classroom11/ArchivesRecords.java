package br.edu.cederj.poo.classroom11;

import java.io.*;

public class ArchivesRecords implements Serializable {

    private int id;
    private float grade;
    private static int amount = 0;

    public ArchivesRecords(float grade) {
        amount++;
        id = amount;
        this.grade = grade;
    }

    public static void writesRecords() {

        try {

            FileOutputStream fileOutputStream = new FileOutputStream("src/resources/data.dat");
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);

            for (int i = 1; i <= 10; i++) {

                ArchivesRecords registros = new ArchivesRecords(i);
                objectOutputStream.writeObject(registros);
            }

            objectOutputStream.close();
            fileOutputStream.close();

        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }

    public static void readsRecords() {

        try {

            FileInputStream fileInputStream = new FileInputStream("src/resources/data.dat");
            ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);

            for (int i = 1; i <= 10; i++) {
                ArchivesRecords registros = (ArchivesRecords) objectInputStream.readObject();
                System.out.println("Id: " + registros.id);
                System.out.println("Nota: " + registros.grade);
            }

            objectInputStream.close();
            fileInputStream.close();

        } catch (IOException | ClassNotFoundException ioe) {
            ioe.printStackTrace();
        }
    }

    public static void main(String[] args) {
        writesRecords();
        readsRecords();
    }

}
