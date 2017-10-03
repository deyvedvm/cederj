package br.edu.cederj.poo.ap120171;
/**
 * Created by deyve on 07/05/17.
 */
public class Data {

    private int dia;

    private int mes;

    private int ano;

    /**
     *
     */
    public Data (){
        this.dia = 01;
        this.mes = 01;
        this.ano = 1900;
    }

    /**
     * @param dia
     * @param mes
     * @param ano
     */
    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    public void incrementar(){

        this.dia += 1;

    }

    @Override
    public String toString() {

        return dia + " de " + mes + " de " + ano;

    }
}
