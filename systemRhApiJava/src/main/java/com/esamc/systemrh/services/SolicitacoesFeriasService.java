package com.esamc.systemrh.services;

import com.esamc.systemrh.models.entities.Funcionario;
import com.esamc.systemrh.models.entities.SolicitacoesFerias;
import com.esamc.systemrh.models.entities.SolicitacoesFerias;
import com.esamc.systemrh.models.repositories.FuncionarioRepository;
import com.esamc.systemrh.models.repositories.SolicitacoesFeriasRepository;
import com.esamc.systemrh.models.repositories.SolicitacoesFeriasRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SolicitacoesFeriasService {

    @Autowired
    private SolicitacoesFeriasRepository solicitacaoFeriasRepository;

    @Autowired
    private FuncionarioRepository funcionarioRepository;

    // SOLICITAR FÉRIAS
    public SolicitacoesFerias solicitarFerias(
            Integer funcionarioId,
            String dataInicio,
            String dataFim
    ) {

        Funcionario funcionario =
                funcionarioRepository.findById(funcionarioId)
                        .orElse(null);

        if (funcionario == null) {
            return null;
        }

        SolicitacoesFerias ferias = new SolicitacoesFerias();

        ferias.setFuncionario(funcionario);
        ferias.setDataInicio(dataInicio);
        ferias.setDataFim(dataFim);

        return solicitacaoFeriasRepository.save(ferias);
    }

    // LISTAR FÉRIAS
    public List<SolicitacoesFerias> listarFerias() {

        return solicitacaoFeriasRepository.findAll();
    }
}