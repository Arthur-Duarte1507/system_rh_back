package com.esamc.systemrh.models.repositories;

import com.esamc.systemrh.models.entities.Cargo;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CargoRepository extends JpaRepository<Cargo, Integer> {
    Cargo findByNome(String nome);
}
