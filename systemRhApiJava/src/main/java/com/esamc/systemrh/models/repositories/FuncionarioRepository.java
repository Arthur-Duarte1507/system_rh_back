package com.esamc.systemrh.models.repositories;

import com.esamc.systemrh.models.entities.Funcionario;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FuncionarioRepository extends JpaRepository <Funcionario, Integer> {
    public Funcionario findByEmail(String email);
}
