package com.esamc.systemrh.services;

import com.esamc.systemrh.models.entities.Funcionario;
import com.esamc.systemrh.models.entities.Notificacao;
import com.esamc.systemrh.models.repositories.FuncionarioRepository;
import com.esamc.systemrh.models.repositories.NotificacaoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NotificacaoService {

    @Autowired
    private NotificacaoRepository notificacaoRepository;

    @Autowired
    private FuncionarioRepository funcionarioRepository;

    // CRIAR NOTIFICAÇÃO
    public Notificacao criarNotificacao(
            Integer funcionarioId,
            String titulo,
            String mensagem
    ) {

        Funcionario funcionario =
                funcionarioRepository.findById(funcionarioId)
                        .orElse(null);

        if (funcionario == null) {
            return null;
        }

        Notificacao notificacao = new Notificacao();

        notificacao.setFuncionario(funcionario);
        notificacao.setTitulo(titulo);
        notificacao.setMensagem(mensagem);

        return notificacaoRepository.save(notificacao);
    }

    // LISTAR NOTIFICAÇÕES
    public List<Notificacao> listarNotificacoes() {

        return notificacaoRepository.findAll();
    }

    // BUSCAR NOTIFICAÇÃO POR ID
    public Notificacao buscarNotificacaoPorId(
            Integer notificacaoId
    ) {

        return notificacaoRepository
                .findById(notificacaoId)
                .orElse(null);
    }

    // MARCAR COMO LIDA
    public Notificacao marcarComoLida(
            Notificacao notificacao
    ) {

        notificacao.setLida(true);

        return notificacaoRepository.save(notificacao);
    }

    // DELETAR NOTIFICAÇÃO
    public Boolean deletarNotificacao(
            Notificacao notificacao
    ) {

        notificacaoRepository.delete(notificacao);

        return true;
    }
}