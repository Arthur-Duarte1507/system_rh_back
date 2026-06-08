package com.esamc.systemrh.models.entities;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;

@Entity
@Table(name = "ajustes_ponto_horarios")
public class AjustePontoHorario {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @JsonIgnore
    @ManyToOne
    @JoinColumn(name = "ajuste_ponto_id", nullable = false)
    private AjustePonto ajustePonto;

    @Column(nullable = false)
    private String tipo;

    @Column(nullable = false)
    private String horario;

    @Column(nullable = false)
    private Integer ordem;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public AjustePonto getAjustePonto() {
        return ajustePonto;
    }

    public void setAjustePonto(AjustePonto ajustePonto) {
        this.ajustePonto = ajustePonto;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getHorario() {
        return horario;
    }

    public void setHorario(String horario) {
        this.horario = horario;
    }

    public Integer getOrdem() {
        return ordem;
    }

    public void setOrdem(Integer ordem) {
        this.ordem = ordem;
    }
}
