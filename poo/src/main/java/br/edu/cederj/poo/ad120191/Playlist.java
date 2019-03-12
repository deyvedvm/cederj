package br.edu.cederj.poo.ad120191;

public class Playlist {

    int tamanho;

    Midia[] midias;

    public Playlist(int capacidade) {
        this.midias = new Midia[capacidade];
        this.tamanho = 0;
    }

    public boolean inserirMidia(Midia midia) {

        if (this.tamanho < this.midias.length) {

            this.midias[this.tamanho] = midia;
            this.tamanho++;
            return true;

        } else {
            return false;
        }
    }

    public Integer duracaoDaPlaylist() {

        Integer duracaoDaPlaylist = 0;

        for (Midia midia : midias) {

            if (midia != null) {

                duracaoDaPlaylist += midia.getDuracao();
            }
        }

        return duracaoDaPlaylist;
    }

    @Override
    public String toString() {

        Integer horas = duracaoDaPlaylist() / 60;

        Integer minutos = duracaoDaPlaylist() % 60;

        return horas.toString() + "h" + " e " + minutos.toString() + "min";
    }
}
