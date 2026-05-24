package com.esamc.systemrh.controller;

import com.esamc.systemrh.models.dtos.AjustePontoRequest;
import com.esamc.systemrh.models.entities.AjustePonto;
import com.esamc.systemrh.models.entities.RegistroPonto;
import com.esamc.systemrh.services.AjustePontoService;
import com.esamc.systemrh.services.RegistroPontoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
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

        ajustePonto.setStatus("Aprovado");

        LocalDate data =
                ajustePonto.getDataAjuste()
                        .toLocalDateTime()
                        .toLocalDate();

        LocalDateTime horaInicial =
                LocalDateTime.of(
                        data,
                        LocalTime.parse(
                                ajustePonto.getHoraInicial()
                        )
                );

        LocalDateTime intervaloInicial =
                LocalDateTime.of(
                        data,
                        LocalTime.parse(
                                ajustePonto.getIntervaloInicial()
                        )
                );

        LocalDateTime intervaloFinal =
                LocalDateTime.of(
                        data,
                        LocalTime.parse(
                                ajustePonto.getIntervaloFinal()
                        )
                );

        LocalDateTime horaFinal =
                LocalDateTime.of(
                        data,
                        LocalTime.parse(
                                ajustePonto.getHoraFinal()
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

    @GetMapping("/solicitacoesAjuste")
    public List<AjustePonto> solicitacoesDeAjuste(){
        return ajustePontoService.FindAll();
    }

}
