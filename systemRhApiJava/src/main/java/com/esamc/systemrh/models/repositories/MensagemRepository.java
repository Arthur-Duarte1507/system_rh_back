package com.esamc.systemrh.models.repositories;

import com.esamc.systemrh.models.entities.AjustePonto;
import com.esamc.systemrh.models.entities.Mensagem;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface MensagemRepository extends JpaRepository<Mensagem, Integer> {
    public List<Mensagem> findByConversaId(Integer conversaId);
}
