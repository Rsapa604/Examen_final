import unittest
from src.proceso import Proceso
from src.metrics import calcular_metricas

class TestMetrics(unittest.TestCase):
    def test_metricas_basicas(self):
        p1 = Proceso("P1", 4, 1)
        p1.tiempo_inicio = 0
        p1.tiempo_fin = 4

        p2 = Proceso("P2", 3, 2)
        p2.tiempo_inicio = 4
        p2.tiempo_fin = 7

        resultados = calcular_metricas([p1, p2])
        self.assertAlmostEqual(resultados["promedio_respuesta"], 2.0)
        self.assertAlmostEqual(resultados["promedio_retorno"], 7.0 / 2)
        self.assertAlmostEqual(resultados["promedio_espera"], 1.0)