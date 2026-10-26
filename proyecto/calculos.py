def calcular_puntos(goles_favor: int, goles_contra: int) -> int:
    if goles_favor < 0 or goles_contra < 0:
        raise ValueError("Los goles no pueden ser valores negativos")

    if goles_favor > goles_contra:
        return 3
    elif goles_favor == goles_contra:
        return 1
    else:
        return 0


def calcular_diferencia_gol(goles_favor: int, goles_contra: int) -> int:
    if goles_favor < 0 or goles_contra < 0:
        raise ValueError("Los goles no pueden ser valores negativos")
    return goles_favor - goles_contra


def determinar_resultado(goles_local: int, goles_visitante: int) -> str:
    if goles_local < 0 or goles_visitante < 0:
        raise ValueError("Los goles no pueden ser valores negativos")

    if goles_local > goles_visitante:
        return "LOCAL"
    elif goles_visitante > goles_local:
        return "VISITANTE"
    else:
        return "EMPATE"


def calcular_promedio_gol(goles_totales: int, partidos_jugados: int) -> float:
    if goles_totales < 0:
        raise ValueError("Los goles no pueden ser negativos")
    if partidos_jugados <= 0:
        raise ValueError("Los partidos jugados deben ser mayores a cero")
    return round(goles_totales / partidos_jugados, 2)


def actualizar_estadisticas_equipo(stats_actuales: dict, goles_favor: int, goles_contra: int) -> dict:
    puntos = calcular_puntos(goles_favor, goles_contra)
    dif_gol = calcular_diferencia_gol(goles_favor, goles_contra)

    stats = stats_actuales.copy()
    stats["pj"] = stats.get("pj", 0) + 1
    stats["gf"] = stats.get("gf", 0) + goles_favor
    stats["gc"] = stats.get("gc", 0) + goles_contra
    stats["dif_gol"] = stats.get("dif_gol", 0) + dif_gol
    stats["puntos"] = stats.get("puntos", 0) + puntos

    if puntos == 3:
        stats["pg"] = stats.get("pg", 0) + 1
    elif puntos == 1:
        stats["pe"] = stats.get("pe", 0) + 1
    else:
        stats["pp"] = stats.get("pp", 0) + 1

    return stats


def ordenar_tabla_posiciones(tabla: list[dict]) -> list[dict]:
    return sorted(
        tabla,
        key=lambda equipo: (
            equipo.get("puntos", 0),
            equipo.get("dif_gol", 0),
            equipo.get("gf", 0),
        ),
        reverse=True,
    )
