def calcular_metricas(procesos):
    n = len(procesos)
    total_respuesta = 0
    total_retorno = 0
    total_espera = 0

    for p in procesos:
        respuesta = p.tiempo_inicio - p.tiempo_llegada
        retorno = p.tiempo_fin - p.tiempo_llegada
        espera = retorno - p.duracion

        total_respuesta += respuesta
        total_retorno += retorno
        total_espera += espera