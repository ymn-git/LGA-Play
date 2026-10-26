import pytest
from calculos import (
    calcular_puntos,
    calcular_diferencia_gol,
    determinar_resultado,
    calcular_promedio_gol,
    actualizar_estadisticas_equipo,
    ordenar_tabla_posiciones,
)

def test_calcular_puntos_victoria():
    """Un equipo que gana el partido debe recibir 3 puntos."""
    assert calcular_puntos(goles_favor=3, goles_contra=1) == 3


def test_calcular_puntos_empate():
    """Un empate debe otorgar 1 punto a cada equipo."""
    assert calcular_puntos(goles_favor=2, goles_contra=2) == 1
    assert calcular_puntos(goles_favor=0, goles_contra=0) == 1


def test_calcular_puntos_derrota():
    """Una derrota debe otorgar 0 puntos."""
    assert calcular_puntos(goles_favor=0, goles_contra=2) == 0


def test_calcular_puntos_con_goles_negativos_lanza_error():
    """No se deben permitir goles con valores negativos (caso inválido)."""
    with pytest.raises(ValueError, match="Los goles no pueden ser valores negativos"):
        calcular_puntos(goles_favor=-1, goles_contra=2)


def test_calcular_diferencia_gol_positiva():
    """Diferencia favorable cuando se anotan más goles de los recibidos."""
    assert calcular_diferencia_gol(goles_favor=4, goles_contra=1) == 3


def test_calcular_diferencia_gol_negativa():
    """Diferencia negativa cuando se reciben más goles de los anotados."""
    assert calcular_diferencia_gol(goles_favor=1, goles_contra=3) == -2


def test_calcular_diferencia_gol_cero():
    """Diferencia neutra en caso de empate."""
    assert calcular_diferencia_gol(goles_favor=2, goles_contra=2) == 0


def test_determinar_resultado():
    """Comprueba el ganador correcto según el marcador."""
    assert determinar_resultado(goles_local=2, goles_visitante=0) == "LOCAL"
    assert determinar_resultado(goles_local=1, goles_visitante=3) == "VISITANTE"
    assert determinar_resultado(goles_local=1, goles_visitante=1) == "EMPATE"


def test_calcular_promedio_gol():
    """Cálculo correcto del promedio de gol por partido."""
    # 10 goles en 4 partidos = 2.5 goles/partido
    assert calcular_promedio_gol(goles_totales=10, partidos_jugados=4) == 2.50


def test_calcular_promedio_gol_sin_partidos_lanza_error():
    """No se puede calcular el promedio si el equipo no disputó partidos (división por cero)."""
    with pytest.raises(ValueError, match="Los partidos jugados deben ser mayores a cero"):
        calcular_promedio_gol(goles_totales=0, partidos_jugados=0)


def test_actualizar_estadisticas_equipo_victoria():
    """Verifica que tras una victoria se actualicen correctamente PJ, PG, GF, GC, dif_gol y puntos."""
    stats_iniciales = {"pj": 0, "pg": 0, "pe": 0, "pp": 0, "gf": 0, "gc": 0, "dif_gol": 0, "puntos": 0}
    nuevas_stats = actualizar_estadisticas_equipo(stats_iniciales, goles_favor=3, goles_contra=1)

    assert nuevas_stats["pj"] == 1
    assert nuevas_stats["pg"] == 1
    assert nuevas_stats["pe"] == 0
    assert nuevas_stats["pp"] == 0
    assert nuevas_stats["gf"] == 3
    assert nuevas_stats["gc"] == 1
    assert nuevas_stats["dif_gol"] == 2
    assert nuevas_stats["puntos"] == 3


def test_ordenar_tabla_posiciones_criterios_liga():
    """
    Verifica que la tabla ordene primero por puntos, luego por diferencia de gol
    y finalmente por goles a favor.
    """
    tabla_desordenada = [
        {"nombre": "Equipo B", "puntos": 6, "dif_gol": 2, "gf": 5},
        {"nombre": "Equipo A", "puntos": 9, "dif_gol": 5, "gf": 8},
        {"nombre": "Equipo C", "puntos": 6, "dif_gol": 4, "gf": 6},  # Mismos puntos que B, mejor dif_gol
        {"nombre": "Equipo D", "puntos": 6, "dif_gol": 4, "gf": 7},  # Mismos puntos y dif_gol que C, más gf
    ]

    tabla_ordenada = ordenar_tabla_posiciones(tabla_desordenada)

    nombres_ordenados = [e["nombre"] for e in tabla_ordenada]
    assert nombres_ordenados == ["Equipo A", "Equipo D", "Equipo C", "Equipo B"]
