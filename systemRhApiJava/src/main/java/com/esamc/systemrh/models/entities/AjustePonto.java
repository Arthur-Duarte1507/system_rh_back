package com.esamc.systemrh.models.entities;
import jakarta.persistence.*;

import java.sql.Timestamp;

@Entity
@Table(name = "ajustes_ponto")
public class AjustePonto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "funcionario_id")
    private Funcionario funcionario;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String motivo;

    @Column(name = "status")
    private String status = "pendente";

    @Column(name = "data_ajustada")
    private Timestamp dataAjuste;

    @Column(name = "hora_inicial")
    private String horaInicial;

    @Column(name = "intervalo_inicial")
    private String intervaloInicial;

    @Column(name = "intervalo_final")
    private String intervaloFinal;

    @Column(name = "hora_final")
    private String horaFinal;

    public Timestamp getDataAjuste() {
        return dataAjuste;
    }

    public void setDataAjuste(Timestamp dataAjuste) {
        this.dataAjuste = dataAjuste;
    }

    public String getHoraInicial() {
        return horaInicial;
    }

    public void setHoraInicial(String horaInicial) {
        this.horaInicial = horaInicial;
    }

    public String getIntervaloInicial() {
        return intervaloInicial;
    }

    public void setIntervaloInicial(String intervaloInicial) {
        this.intervaloInicial = intervaloInicial;
    }

    public String getIntervaloFinal() {
        return intervaloFinal;
    }

    public void setIntervaloFinal(String intervaloFinal) {
        this.intervaloFinal = intervaloFinal;
    }

    public String getHoraFinal() {
        return horaFinal;
    }

    public void setHoraFinal(String horaFinal) {
        this.horaFinal = horaFinal;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Funcionario getFuncionario() {
        return funcionario;
    }

    public void setFuncionario(Funcionario funcionario) {
        this.funcionario = funcionario;
    }

    public String getMotivo() {
        return motivo;
    }

    public void setMotivo(String motivo) {
        this.motivo = motivo;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}