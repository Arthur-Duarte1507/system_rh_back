package com.esamc.systemrh.models.dtos;

import com.fasterxml.jackson.annotation.JsonFormat;

import java.time.LocalDate;

public class AjustePontoRequest {

    private Integer funcionarioId;

    private String motivo;

    @JsonFormat(pattern = "dd/MM/yyyy")
    private LocalDate dataAjuste;

    private String horaInicial;

    private String intervaloInicial;

    private String intervaloFinal;

    private String horaFinal;

    public Integer getFuncionarioId() {
        return funcionarioId;
    }

    public void setFuncionarioId(Integer funcionarioId) {
        this.funcionarioId = funcionarioId;
    }

    public String getMotivo() {
        return motivo;
    }

    public void setMotivo(String motivo) {
        this.motivo = motivo;
    }

    public LocalDate getDataAjuste() {
        return dataAjuste;
    }

    public void setDataAjuste(LocalDate dataAjuste) {
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
}