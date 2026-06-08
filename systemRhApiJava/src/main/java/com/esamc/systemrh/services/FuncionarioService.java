package com.esamc.systemrh.services;

import com.esamc.systemrh.models.entities.Cargo;
import com.esamc.systemrh.models.entities.Funcionario;
import com.esamc.systemrh.models.repositories.CargoRepository;
import com.esamc.systemrh.models.repositories.FuncionarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.List;

@Service
public class FuncionarioService {

    @Autowired
    FuncionarioRepository funcionarioRepository;

    @Autowired
    CargoRepository cargoRepository;

    private Cargo buscarOuCriarCargo(String nome) {
        String nomeCargo =
                nome == null || nome.trim().isEmpty()
                        ? "Funcionario"
                        : nome.trim();

        Cargo cargo = cargoRepository.findByNome(nomeCargo);

        if (cargo != null) {
            return cargo;
        }

        cargo = new Cargo();
        cargo.setNome(nomeCargo);

        return cargoRepository.save(cargo);
    }

    private LocalDate normalizarData(String valor) {
        if (valor == null || valor.trim().isEmpty()) {
            return null;
        }

        String data = valor.trim();

        DateTimeFormatter[] formatos = new DateTimeFormatter[]{
                DateTimeFormatter.ISO_LOCAL_DATE,
                DateTimeFormatter.ofPattern("dd/MM/yyyy")
        };

        for (DateTimeFormatter formato : formatos) {
            try {
                return LocalDate.parse(data, formato);
            } catch (DateTimeParseException ignored) {
            }
        }

        return null;
    }

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
        funcionario.setCargo(buscarOuCriarCargo(cargo));
        funcionario.setAniversario(aniversario);
        funcionario.setDataAdmissao(normalizarData(tempoCasa));

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
        funcionario.setCargo(buscarOuCriarCargo(cargo));
        funcionario.setAniversario(aniversario);
        funcionario.setDataAdmissao(normalizarData(tempoCasa));

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
