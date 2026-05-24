package com.esamc.systemrh.models.repositories;

import com.esamc.systemrh.models.entities.Conversa;
import com.esamc.systemrh.models.entities.SolicitacoesFerias;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SolicitacoesFeriasRepository extends JpaRepository<SolicitacoesFerias, Integer> {
}
