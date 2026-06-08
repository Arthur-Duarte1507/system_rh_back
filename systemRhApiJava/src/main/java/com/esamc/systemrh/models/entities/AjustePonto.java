package com.esamc.systemrh.models.entities;

import jakarta.persistence.*;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

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

    @OneToMany(
            mappedBy = "ajustePonto",
            cascade = CascadeType.ALL,
            orphanRemoval = true,
            fetch = FetchType.EAGER
    )
    private List<AjustePontoHorario> horarios = new ArrayList<>();

    public void adicionarHorario(
            String tipo,
            String horario,
            Integer ordem
    ) {
        if (horario == null || horario.trim().isEmpty()) {
            return;
        }

        AjustePontoHorario item = new AjustePontoHorario();
        item.setAjustePonto(this);
        item.setTipo(tipo);
        item.setHorario(horario);
        item.setOrdem(ordem);

        horarios.add(item);
    }

    public String buscarHorario(String tipo) {
        return horarios.stream()
                .filter(horario -> tipo.equals(horario.getTipo()))
                .sorted(Comparator.comparing(AjustePontoHorario::getOrdem))
                .map(AjustePontoHorario::getHorario)
                .findFirst()
                .orElse(null);
    }

    public Timestamp getDataAjuste() {
        return dataAjuste;
    }

    public void setDataAjuste(Timestamp dataAjuste) {
        this.dataAjuste = dataAjuste;
    }

    public List<AjustePontoHorario> getHorarios() {
        return horarios;
    }

    public void setHorarios(List<AjustePontoHorario> horarios) {
        this.horarios = horarios;
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
