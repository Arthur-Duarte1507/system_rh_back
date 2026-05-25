package com.esamc.systemrh.controller;

import com.esamc.systemrh.models.dtos.AjustePontoRequest;
import com.esamc.systemrh.models.entities.AjustePonto;
import com.esamc.systemrh.models.entities.RegistroPonto;
import com.esamc.systemrh.services.AjustePontoService;
import com.esamc.systemrh.services.RegistroPontoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.List;

@RestController
@RequestMapping("/api")
@CrossOrigin("*")
public class PontoController {
    @Autowired
    AjustePontoService ajustePontoService;

    @Autowired
    RegistroPontoService registroPontoService;

    @GetMapping("/teste")
    public String teste(){
        return "FUNFANDO";
    }

    @PostMapping("ajustesPonto/ajustePonto")
        public AjustePonto ajustePonto(@RequestBody AjustePontoRequest ajustePontoRequest){
            return (ajustePontoService.saveAjuste(ajustePontoRequest));
    }

    @PostMapping("ajustesPonto/aprovarAjuste/{id}")
    public AjustePonto aprovarAjuste(
            @PathVariable Integer id
    ){

        AjustePonto ajustePonto =
                ajustePontoService.findById(id);

        if (ajustePonto == null) {
            throw new ResponseStatusException(
                    HttpStatus.NOT_FOUND,
                    "Ajuste de ponto nao encontrado para o id " + id
            );
        }

        ajustePonto.setStatus("Aprovado");

        LocalDate data =
                ajustePonto.getDataAjuste()
                        .toLocalDateTime()
                        .toLocalDate();

        LocalDateTime horaInicial =
                LocalDateTime.of(
                        data,
                        parseHorario(
                                ajustePonto.getHoraInicial(),
                                "horaInicial"
                        )
                );

        LocalDateTime intervaloInicial =
                LocalDateTime.of(
                        data,
                        parseHorario(
                                ajustePonto.getIntervaloInicial(),
                                "intervaloInicial"
                        )
                );

        LocalDateTime intervaloFinal =
                LocalDateTime.of(
                        data,
                        parseHorario(
                                ajustePonto.getIntervaloFinal(),
                                "intervaloFinal"
                        )
                );

        LocalDateTime horaFinal =
                LocalDateTime.of(
                        data,
                        parseHorario(
                                ajustePonto.getHoraFinal(),
                                "horaFinal"
                        )
                );

        RegistroPonto r1 =
                new RegistroPonto(
                        ajustePonto.getFuncionario(),
                        horaInicial,
                        "Entrada"
                );

        RegistroPonto r2 =
                new RegistroPonto(
                        ajustePonto.getFuncionario(),
                        intervaloInicial,
                        "Saida"
                );

        RegistroPonto r3 =
                new RegistroPonto(
                        ajustePonto.getFuncionario(),
                        intervaloFinal,
                        "Entrada"
                );

        RegistroPonto r4 =
                new RegistroPonto(
                        ajustePonto.getFuncionario(),
                        horaFinal,
                        "Saida"
                );

        registroPontoService.deletarRegistrosPorData(data);

        registroPontoService.registroPonto(r1);
        registroPontoService.registroPonto(r2);
        registroPontoService.registroPonto(r3);
        registroPontoService.registroPonto(r4);

        return ajustePontoService.saveAjuste(ajustePonto);
    }

    private LocalTime parseHorario(
            String valor,
            String campo
    ) {
        if (valor == null || valor.trim().isEmpty()) {
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Campo " + campo + " nao foi informado."
            );
        }

        String horario = valor.trim().replace('.', ':');

        if (horario.matches("^\\d{1,2}$")) {
            horario = String.format("%02d:00", Integer.parseInt(horario));
        }

        if (horario.matches("^\\d{1,2}:\\d{1,2}$")) {
            String[] partes = horario.split(":");
            horario = String.format(
                    "%02d:%02d",
                    Integer.parseInt(partes[0]),
                    Integer.parseInt(partes[1])
            );
        }

        if (horario.matches("^\\d{1,2}:\\d{1,2}:\\d{1,2}$")) {
            String[] partes = horario.split(":");
            horario = String.format(
                    "%02d:%02d:%02d",
                    Integer.parseInt(partes[0]),
                    Integer.parseInt(partes[1]),
                    Integer.parseInt(partes[2])
            );
        }

        DateTimeFormatter[] formatos = new DateTimeFormatter[]{
                DateTimeFormatter.ofPattern("HH:mm"),
                DateTimeFormatter.ofPattern("HH:mm:ss")
        };

        for (DateTimeFormatter formato : formatos) {
            try {
                return LocalTime.parse(horario, formato);
            } catch (DateTimeParseException ignored) {
            }
        }

        throw new ResponseStatusException(
                HttpStatus.BAD_REQUEST,
                "Campo " + campo + " invalido: '" + valor + "'. Use HH:mm."
        );
    }

    @GetMapping("/solicitacoesAjuste")
    public List<AjustePonto> solicitacoesDeAjuste(){
        return ajustePontoService.FindAll();
    }

}
