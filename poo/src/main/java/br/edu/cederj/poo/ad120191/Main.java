package br.edu.cederj.poo.ad120191;

public class Main {

    public static void main(String[] args) {

        Musica aguaDeBeber = new Musica("Agua de beber", "Antonio Carlos Jobim", "Astrud Gilberto", 140);
        Musica oMarSerenou = new Musica("O mar serenou", "Candeia", "Clara Nunes", 179);
        Musica rapazFolgado = new Musica("Rapaz Folgado", "Noel Rosa", "Martinho da Vila e Mart'nália", 180);

        Playlist playlist = new Playlist(5);

        playlist.inserirMidia(aguaDeBeber);
        playlist.inserirMidia(oMarSerenou);
        playlist.inserirMidia(rapazFolgado);

        System.out.println(playlist);

        Video despacito = new Video("Musica", "Despacito", "Luis Fonsi", 5926796, 280);
        Video gangnamStyle = new Video("Musica", "Gangnam Style", "Officialpsy", 3276192, 252);

        playlist.inserirMidia(despacito);
        playlist.inserirMidia(gangnamStyle);

        System.out.println(playlist);
    }
}
