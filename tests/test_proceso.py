import unittest
from src.proceso import Proceso

class TestProceso(unittest.TestCase):
    def test_creacion_valida(self):
        p = Proceso("P1", 5, 2)
        self.assertEqual(p.pid, "P1")
        self.assertEqual(p.duracion, 5)
        self.assertEqual(p.prioridad, 2)
        self.assertEqual(p.tiempo_restante, 5)