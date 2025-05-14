import unittest
from src.proceso import Proceso
from src.scheduler import FCFSScheduler, RoundRobinScheduler

class TestScheduler(unittest.TestCase):
    def test_fcfs(self):
        procesos = [Proceso("P1", 4, 2), Proceso("P2", 3, 1)]
        scheduler = FCFSScheduler()
        resultado = scheduler.planificar(procesos)
        self.assertEqual(resultado, [("P1", 0, 4), ("P2", 4, 7)])

    def test_rr(self):
        procesos = [Proceso("P1", 5, 1), Proceso("P2", 3, 2)]
        scheduler = RoundRobinScheduler(2)
        resultado = scheduler.planificar(procesos)
        pids = [x[0] for x in resultado]
        self.assertIn("P1", pids)
        self.assertIn("P2", pids)

    def test_rr_quantum_invalido(self):
        with self.assertRaises(ValueError):
            RoundRobinScheduler(0)