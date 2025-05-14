import unittest
import os
from src.proceso import Proceso
from src.repositorio import RepositorioProcesos

class TestRepositorio(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorioProcesos()
        self.p1 = Proceso("P1", 4, 1)
        self.repo.agregar(self.p1)

    def test_agregar_duplicado(self):
        with self.assertRaises(ValueError):
            self.repo.agregar(Proceso("P1", 3, 2))

    def test_eliminar(self):
        self.repo.eliminar("P1")
        self.assertEqual(self.repo.listar(), [])

    def test_guardar_y_cargar_json(self):
        ruta = "test_procesos.json"
        self.repo.guardar_json(ruta)
        nuevo = RepositorioProcesos()
        nuevo.cargar_json(ruta)
        self.assertEqual(len(nuevo.listar()), 1)
        os.remove(ruta)

    def test_guardar_y_cargar_csv(self):
        ruta = "test_procesos.csv"
        self.repo.guardar_csv(ruta)
        nuevo = RepositorioProcesos()
        nuevo.cargar_csv(ruta)
        self.assertEqual(len(nuevo.listar()), 1)
        os.remove(ruta)