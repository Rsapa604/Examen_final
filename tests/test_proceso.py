import unittest
from src.proceso import Proceso

class TestProceso(unittest.TestCase):
    def test_creacion_valida(self):
        p = Proceso("P1", 5, 2)
        self.assertEqual(p.pid, "P1")
        self.assertEqual(p.duracion, 5)
        self.assertEqual(p.prioridad, 2)
        self.assertEqual(p.tiempo_restante, 5)

    def test_pid_vacio(self):
        with self.assertRaises(ValueError):
            Proceso("", 5, 1)

    def test_duracion_invalida(self):
        with self.assertRaises(ValueError):
            Proceso("P2", -3, 1)

    def test_prioridad_invalida(self):
        with self.assertRaises(ValueError):
            Proceso("P3", 5, "alta")