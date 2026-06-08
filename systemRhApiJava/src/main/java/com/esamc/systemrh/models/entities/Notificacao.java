package com.esamc.systemrh.models.entities;

import jakarta.persistence.*;

import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "notificacoes")
public class Notificacao {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(nullable = false)
    private String titulo;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String mensagem;

    private String data;

    @OneToMany(
            mappedBy = "notificacao",
            cascade = CascadeType.ALL,
            orphanRemoval = true,
            fetch = FetchType.EAGER
    )
    private List<NotificacaoDestinatario> destinatarios = new ArrayList<>();

    public void adicionarDestinatario(
            Funcionario funcionario
    ) {
        NotificacaoDestinatario destinatario = new NotificacaoDestinatario();
        destinatario.setNotificacao(this);
        destinatario.setFuncionario(funcionario);
        destinatario.setLida(false);

        destinatarios.add(destinatario);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getMensagem() {
        return mensagem;
    }

    public void setMensagem(String mensagem) {
        this.mensagem = mensagem;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public List<NotificacaoDestinatario> getDestinatarios() {
        return destinatarios;
    }

    public void setDestinatarios(List<NotificacaoDestinatario> destinatarios) {
        this.destinatarios = destinatarios;
    }
}
