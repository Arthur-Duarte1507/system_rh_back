package com.esamc.systemrh.models.repositories;

import com.esamc.systemrh.models.entities.AjustePonto;
import com.esamc.systemrh.models.entities.Notificacao;
import org.springframework.data.jpa.repository.JpaRepository;

public interface NotificacaoRepository extends JpaRepository<Notificacao, Integer> {
}
