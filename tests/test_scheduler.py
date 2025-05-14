import unittest
from src.proceso import Proceso
from src.scheduler import FCFSScheduler, RoundRobinScheduler

class TestScheduler(unittest.TestCase):
    def test_fcfs(self):
        procesos = [Proceso("P1", 4, 2), Proceso("P2", 3, 1)]
        scheduler = FCFSScheduler()
        resultado = scheduler.planificar(procesos)
        self.assertEqual(resultado, [("P1", 0, 4), ("P2", 4, 7)])