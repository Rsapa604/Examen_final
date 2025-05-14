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
class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum):
        if quantum <= 0:
            raise ValueError("El quantum debe ser un entero positivo.")
        self.quantum = quantum

    def planificar(self, procesos):
        copia = []
        for original in procesos:
            p = Proceso(original.pid, original.duracion, original.prioridad)
            copia.append(p)

        tiempo = 0
        gantt = []

        while True:
            activos = [p for p in copia if p.tiempo_restante > 0]
            if not activos:
                break
            for p in activos:
                if p.tiempo_restante > 0:
                    if p.tiempo_inicio is None:
                        p.tiempo_inicio = tiempo
                    ejecutar = min(self.quantum, p.tiempo_restante)
                    gantt.append((p.pid, tiempo, tiempo + ejecutar))
                    tiempo += ejecutar
                    p.tiempo_restante -= ejecutar
                    if p.tiempo_restante == 0:
                        p.tiempo_fin = tiempo
        return gantt