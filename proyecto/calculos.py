"""
Módulo de cálculos y lógica de negocio para la liga deportiva LGA-Play.
Incluye cálculos de puntuaciones de partidos, estadísticas de equipos,
diferencia de gol, tabla de posiciones y promedios.
"""


def calcular_puntos(goles_favor: int, goles_contra: int) -> int:
    """
    Calcula los puntos obtenidos por un equipo en un partido según las reglas de la liga:
    - Victoria: 3 puntos
    - Empate: 1 punto
    - Derrota: 0 puntos
    Lanza ValueError si alguno de los goles es negativo.
    """
    if goles_favor < 0 or goles_contra < 0:
        raise ValueError("Los goles no pueden ser valores negativos")

    if goles_favor > goles_contra:
        return 3
    elif goles_favor == goles_contra:
        return 1
    else:
        return 0


def calcular_diferencia_gol(goles_favor: int, goles_contra: int) -> int:
    """
    Calcula la diferencia de gol (Goles a Favor - Goles en Contra).
    Lanza ValueError si alguno de los goles es negativo.
    """
    if goles_favor < 0 or goles_contra < 0:
        raise ValueError("Los goles no pueden ser valores negativos")
    return goles_favor - goles_contra


def determinar_resultado(goles_local: int, goles_visitante: int) -> str:
    """
    Determina el resultado final de un partido:
    'LOCAL', 'VISITANTE' o 'EMPATE'.
    """
    if goles_local < 0 or goles_visitante < 0:
        raise ValueError("Los goles no pueden ser valores negativos")

    if goles_local > goles_visitante:
        return "LOCAL"
    elif goles_visitante > goles_local:
        return "VISITANTE"
    else:
        return "EMPATE"


def calcular_promedio_gol(goles_totales: int, partidos_jugados: int) -> float:
    """
    Calcula el promedio de gol por partido de un jugador o equipo.
    Lanza ValueError si partidos_jugados <= 0 o si goles_totales < 0.
    """
    if goles_totales < 0:
        raise ValueError("Los goles no pueden ser negativos")
    if partidos_jugados <= 0:
        raise ValueError("Los partidos jugados deben ser mayores a cero")
    return round(goles_totales / partidos_jugados, 2)


def actualizar_estadisticas_equipo(stats_actuales: dict, goles_favor: int, goles_contra: int) -> dict:
    """
    Actualiza las estadísticas de un equipo tras disputar un partido:
    partidos jugados (pj), ganados (pg), empatados (pe), perdidos (pp),
    goles a favor (gf), goles en contra (gc), diferencia de gol (dif_gol) y puntos.
    """
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
    """
    Ordena la tabla de posiciones de la liga bajo los criterios oficiales:
    1. Mayor cantidad de puntos (descendente)
    2. Mayor diferencia de gol (descendente)
    3. Mayor cantidad de goles a favor (descendente)
    """
    return sorted(
        tabla,
        key=lambda equipo: (
            equipo.get("puntos", 0),
            equipo.get("dif_gol", 0),
            equipo.get("gf", 0),
        ),
        reverse=True,
    )
