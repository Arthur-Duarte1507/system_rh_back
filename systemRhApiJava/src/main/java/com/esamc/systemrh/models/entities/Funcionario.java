package com.esamc.systemrh.models.entities;
import jakarta.persistence.*;

@Entity
@Table(name = "funcionarios")
public class Funcionario {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(nullable = false)
    private String nome;

    @Column(unique = true, nullable = false)
    private String email;

    @Column(nullable = false)
    private String senha;

    @Column(nullable = false)
    private String cargo;

    @Column(nullable = false)
    private String tempo_casa;

    @Column(nullable = false)
    private String aniversario;

    @Column(name = "estado_trabalho", nullable = false, length = 50)
    private String estadoTrabalho = "nao_comecou";

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public String getTempo_casa() {
        return tempo_casa;
    }

    public void setTempo_casa(String tempo_casa) {
        this.tempo_casa = tempo_casa;
    }

    public String getAniversario() {
        return aniversario;
    }

    public void setAniversario(String aniversario) {
        this.aniversario = aniversario;
    }

    public String getEstadoTrabalho() {
        return estadoTrabalho;
    }

    public void setEstadoTrabalho(String estadoTrabalho) {
        this.estadoTrabalho = estadoTrabalho;
    }
}
