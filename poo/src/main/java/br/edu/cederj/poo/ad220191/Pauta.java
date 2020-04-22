package br.edu.cederj.poo.ad220191;

public class Pauta {

    private String descricao;

    private Integer mesInicio;

    private Integer mesFim;

    private Aluno[] alunos;

    public Pauta(int mesInicio, int mesFim, Turma turma) {
        this.mesInicio = mesInicio;
        this.mesFim = mesFim;
        this.alunos = turma.getAlunos();
    }

    public void marcarFalta(Integer matricula, Integer mes, Integer dia) {


    }

    public int totalFaltasAluno(Integer matricula) {

        return 0;
    }

    public boolean verificarReprovacaoPorFalta(Integer matricula) {
        return false;
    }

    public void imprimir() {

    }
}
