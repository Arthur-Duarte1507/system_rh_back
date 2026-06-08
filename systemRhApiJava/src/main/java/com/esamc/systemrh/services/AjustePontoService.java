package com.esamc.systemrh.services;

import com.esamc.systemrh.models.dtos.AjustePontoRequest;
import com.esamc.systemrh.models.entities.AjustePonto;
import com.esamc.systemrh.models.entities.Funcionario;
import com.esamc.systemrh.models.repositories.AjustePontoRepository;
import com.esamc.systemrh.models.repositories.FuncionarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AjustePontoService {

    @Autowired
    AjustePontoRepository ajustePontoRepository;

    @Autowired
    FuncionarioRepository funcionarioRepository;

    public AjustePonto saveAjuste(AjustePonto ajustePonto) {
        return ajustePontoRepository.save(ajustePonto);
    }

    public AjustePonto saveAjuste(
            AjustePontoRequest request
    ){

        Funcionario funcionario =
                funcionarioRepository.findById(
                        request.getFuncionarioId()
                ).orElse(null);

        if (funcionario == null) {
            return null;
        }

        AjustePonto ajuste = new AjustePonto();

        ajuste.setFuncionario(funcionario);

        ajuste.setMotivo(request.getMotivo());

        ajuste.setDataAjuste(
                java.sql.Timestamp.valueOf(
                        request.getDataAjuste()
                                .atStartOfDay()
                )
        );

        ajuste.adicionarHorario(
                "hora_inicial",
                request.getHoraInicial(),
                1
        );

        ajuste.adicionarHorario(
                "intervalo_inicial",
                request.getIntervaloInicial(),
                2
        );

        ajuste.adicionarHorario(
                "intervalo_final",
                request.getIntervaloFinal(),
                3
        );

        ajuste.adicionarHorario(
                "hora_final",
                request.getHoraFinal(),
                4
        );

        return ajustePontoRepository.save(ajuste);
    }

    // LISTAR AJUSTES
    public List<AjustePonto> FindAll() {

        return ajustePontoRepository.findAll();
    }

    // BUSCAR AJUSTE POR ID
    public AjustePonto findById(Integer ajusteId) {

        return ajustePontoRepository
                .findById(ajusteId)
                .orElse(null);
    }
}
