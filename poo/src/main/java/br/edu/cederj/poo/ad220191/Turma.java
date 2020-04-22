package br.edu.cederj.poo.ad220191;

import java.util.Arrays;

public class Turma {

    private String nome;

    private String codigo;

    private String periodo;

    private Aluno[] alunos;

    private Integer tamanho;

    public Turma(String nome, String codigo, String periodo, Integer tamanho) {
        this.nome = nome;
        this.codigo = codigo;
        this.periodo = periodo;
        this.tamanho = 0;
        this.alunos = new Aluno[tamanho];
    }

    public boolean inserirAluno(Aluno aluno) {

        if (this.tamanho < this.alunos.length) {

            this.alunos[this.tamanho] = aluno;
            this.tamanho++;
            return true;

        } else {
            return false;
        }

    }

    public void imprimir() {

        System.out.println(this.toString());
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getPeriodo() {
        return periodo;
    }

    public void setPeriodo(String periodo) {
        this.periodo = periodo;
    }

    public Aluno[] getAlunos() {

        Aluno[] alunos = new Aluno[tamanho];

        for (Aluno aluno : this.alunos) {

            if (aluno != null) {
            }
        }

        return alunos;
    }

    public void setAlunos(Aluno[] alunos) {
        this.alunos = alunos;
    }

    public Integer getTamanho() {
        return tamanho;
    }

    public void setTamanho(Integer tamanho) {
        this.tamanho = tamanho;
    }

    @Override
    public String toString() {
        return "Turma{" +
                "nome='" + nome + '\'' +
                ", codigo='" + codigo + '\'' +
                ", periodo='" + periodo + '\'' +
                ", alunos=" + Arrays.toString(alunos) +
                ", tamanho=" + tamanho +
                '}';
    }
}
