package com.esamc.systemrh.models.repositories;

import com.esamc.systemrh.models.entities.RegistroPonto;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDateTime;
import java.util.List;

public interface RegistroPontoRepository
        extends JpaRepository<RegistroPonto, Integer> {

    List<RegistroPonto> findByFuncionarioId(
            Integer funcionarioId
    );

    RegistroPonto findTopByFuncionarioIdOrderByDataHoraDesc(
            Integer funcionarioId
    );

    void deleteByDataHoraBetween(
            LocalDateTime inicio,
            LocalDateTime fim
    );

}