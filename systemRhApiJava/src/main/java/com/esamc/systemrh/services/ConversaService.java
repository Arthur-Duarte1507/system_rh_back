package com.esamc.systemrh.services;

import com.esamc.systemrh.models.entities.Conversa;
import com.esamc.systemrh.models.entities.Funcionario;
import com.esamc.systemrh.models.entities.Mensagem;
import com.esamc.systemrh.models.repositories.ConversaRepository;
import com.esamc.systemrh.models.repositories.FuncionarioRepository;
import com.esamc.systemrh.models.repositories.MensagemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ConversaService {

    @Autowired
    ConversaRepository conversaRepository;

    // CRIAR CONVERSA
    public Conversa criarConversa(
            String titulo
    ) {

        Conversa conversa = new Conversa();

        conversa.setTitulo(titulo);

        return conversaRepository.save(conversa);
    }

    // LISTAR CONVERSAS
    public List<Conversa> listarConversas() {

        return conversaRepository.findAll();
    }

    // BUSCAR CONVERSA POR ID
    public Conversa buscarConversaPorId(
            Integer conversaId
    ) {

        return conversaRepository
                .findById(conversaId)
                .orElse(null);
    }
}