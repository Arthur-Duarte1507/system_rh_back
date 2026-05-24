package com.esamc.systemrh.services;

import com.esamc.systemrh.models.entities.Funcionario;
import com.esamc.systemrh.models.repositories.FuncionarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class FuncionarioService {

    @Autowired
    FuncionarioRepository funcionarioRepository;

    // BUSCAR FUNCIONÁRIO POR ID
    public Funcionario buscarFuncionarioPorId(
            Integer funcionarioId
    ) {

        return funcionarioRepository
                .findById(funcionarioId)
                .orElse(null);
    }

    // LISTAR FUNCIONÁRIOS
    public List<Funcionario> listarFuncionarios() {

        return funcionarioRepository.findAll();
    }

    // CRIAR FUNCIONÁRIO
    public Funcionario criarFuncionario(
            String nome,
            String email,
            String senha,
            String cargo,
            String tempoCasa,
            String aniversario,
            String estadoTrabalho
    ) {

        Funcionario funcionario = new Funcionario();

        funcionario.setNome(nome);
        funcionario.setEmail(email);
        funcionario.setSenha(senha);
        funcionario.setCargo(cargo);
        funcionario.setTempo_casa(tempoCasa);
        funcionario.setAniversario(aniversario);

        funcionario.setEstadoTrabalho(
                estadoTrabalho != null
                        ? estadoTrabalho
                        : "nao_comecou"
        );

        return funcionarioRepository.save(funcionario);
    }

    // BUSCAR FUNCIONÁRIO POR EMAIL
    public Funcionario buscarFuncionarioPorEmail(
            String email
    ) {

        return funcionarioRepository.findByEmail(email);
    }

    // ALTERAR FUNCIONÁRIO
    public Funcionario alterarFuncionario(
            Funcionario funcionario,
            String nome,
            String email,
            String cargo,
            String tempoCasa,
            String aniversario,
            String estadoTrabalho
    ) {

        funcionario.setNome(nome);
        funcionario.setEmail(email);
        funcionario.setCargo(cargo);
        funcionario.setTempo_casa(tempoCasa);
        funcionario.setAniversario(aniversario);
        funcionario.setEstadoTrabalho(estadoTrabalho);

        return funcionarioRepository.save(funcionario);
    }

    // DELETAR FUNCIONÁRIO
    public Boolean deletarFuncionario(
            Funcionario funcionario
    ) {

        funcionarioRepository.delete(funcionario);

        return true;
    }
}