package com.esamc.systemrh.services;

import com.esamc.systemrh.models.entities.Funcionario;
import com.esamc.systemrh.models.entities.RegistroPonto;
import com.esamc.systemrh.models.repositories.FuncionarioRepository;
import com.esamc.systemrh.models.repositories.RegistroPontoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class RegistroPontoService {

    @Autowired
    private RegistroPontoRepository registroPontoRepository;

    @Autowired
    private FuncionarioRepository funcionarioRepository;

    // REGISTRAR PONTO
    public RegistroPonto registrarPontoCorrente(
            Integer funcionarioId,
            String tipo
    ) {

        Funcionario funcionario =
                funcionarioRepository.findById(funcionarioId)
                        .orElse(null);

        if (funcionario == null) {
            return null;
        }

        RegistroPonto registro = new RegistroPonto();
        registro.setDataHora(LocalDateTime.now());
        registro.setFuncionario(funcionario);
        registro.setTipo(tipo);

        return registroPontoRepository.save(registro);
    }

    public RegistroPonto registroPonto (RegistroPonto registroPonto){
        return registroPontoRepository.save(registroPonto);
    }

    // LISTAR PONTOS DO FUNCIONÁRIO
    public List<RegistroPonto> listarPontosFuncionario(
            Integer funcionarioId
    ) {

        return registroPontoRepository
                .findByFuncionarioId(funcionarioId);
    }

    // BUSCAR ÚLTIMO PONTO
    public RegistroPonto buscarUltimoPonto(
            Integer funcionarioId
    ) {

        return registroPontoRepository
                .findTopByFuncionarioIdOrderByDataHoraDesc(
                        funcionarioId
                );
    }

    @Transactional
    public void deletarRegistrosPorData(
            LocalDate data
    ) {

        LocalDateTime inicio =
                data.atStartOfDay();

        LocalDateTime fim =
                data.plusDays(1).atStartOfDay();

        registroPontoRepository
                .deleteByDataHoraBetween(
                        inicio,
                        fim
                );
    }
}
