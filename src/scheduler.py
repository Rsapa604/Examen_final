from src.proceso import Proceso
class Scheduler:
    def planificar(self, procesos):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


class FCFSScheduler(Scheduler):
    def planificar(self, procesos):
        tiempo = 0
        gantt = []
        for p in procesos:
            p.tiempo_inicio = tiempo
            tiempo += p.duracion
            p.tiempo_fin = tiempo
            gantt.append((p.pid, p.tiempo_inicio, p.tiempo_fin))
        return gantt