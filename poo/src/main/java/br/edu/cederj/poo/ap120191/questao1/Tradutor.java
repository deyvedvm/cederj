package br.edu.cederj.poo.ap120191.questao1;

class Tradutor {

    private Entrada[] entradas;
    private int tamanho;
    private static int MAX = 1000;

    public Tradutor() {
        entradas = new Entrada[MAX];
        tamanho = 0;
    }

    public void adiciona(Entrada entrada) {
        if (tamanho < MAX - 1) {
            entradas[tamanho] = entrada;
            tamanho++;
        }
    }

    public String geraEntradas(String idiomaOrigem, String idiomaDestino) {

        StringBuilder saida = new StringBuilder(idiomaOrigem + " -> " + idiomaDestino + "\n");

        for (int index = 0; index < tamanho; index++) {

            if ((entradas[index].getIdiomaOrigem().equals(idiomaOrigem)) && (entradas[index].getIdiomaTraducao().equals(idiomaDestino))) {

                saida.append(entradas[index].getPalavaOrigem()).append(" -> ").append(entradas[index].getPalavraTraducao()).append("\n");

            } else if ((entradas[index].getIdiomaOrigem().equals(idiomaDestino) && entradas[index].getIdiomaTraducao().equals(idiomaOrigem))) {

                saida.append(entradas[index].getPalavraTraducao()).append(" -> ").append(entradas[index].getPalavaOrigem()).append("\n");
            }
        }

        return saida.toString();
    }
}
