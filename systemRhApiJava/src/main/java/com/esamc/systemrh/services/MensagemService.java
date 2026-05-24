package com.esamc.systemrh.services;

import com.esamc.systemrh.models.entities.Conversa;
import com.esamc.systemrh.models.entities.Funcionario;
import com.esamc.systemrh.models.entities.Mensagem;
import com.esamc.systemrh.models.repositories.ConversaRepository;
import com.esamc.systemrh.models.repositories.FuncionarioRepository;
import com.esamc.systemrh.models.repositories.MensagemRepository;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

public class MensagemService {

    @Autowired
    ConversaRepository conversaRepository;

    @Autowired
    MensagemRepository mensagemRepository;

    @Autowired
    FuncionarioRepository funcionarioRepository;

    // ENVIAR MENSAGEM
    public Mensagem enviarMensagem(
            Integer conversaId,
            Integer funcionarioId,
            String texto
    ) {

        Conversa conversa =
                conversaRepository.findById(conversaId).orElse(null);

        Funcionario funcionario =
                funcionarioRepository.findById(funcionarioId)
                        .orElse(null);

        if (conversa == null || funcionario == null) {
            return null;
        }

        Mensagem mensagem = new Mensagem();

        mensagem.setConversa(conversa);
        mensagem.setFuncionario(funcionario);
        mensagem.setTexto(texto);

        return mensagemRepository.save(mensagem);
    }

    // LISTAR MENSAGENS DA CONVERSA
    public List<Mensagem> listarMensagensDaConversa(
            Integer conversaId
    ) {

        return mensagemRepository
                .findByConversaId(conversaId);
    }
}
