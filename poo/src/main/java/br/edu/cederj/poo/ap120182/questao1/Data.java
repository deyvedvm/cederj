package br.edu.cederj.poo.ap120182.questao1;

public class Data {

    int dia;

    int mes;

    int ano;

    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    @Override
    public String toString() {

        return dia + "/" + mes + "/" + ano;
    }

    public int compara(Data data) {

        if (dia == data.dia && mes == data.mes && ano == data.ano) {
            return 0;
        } else if (ano < data.ano || (ano == data.ano && mes < data.mes) || (ano == data.ano && mes == data.mes && dia < data.dia)) {
            return -1;
        } else {
            return 1;
        }
    }
}
