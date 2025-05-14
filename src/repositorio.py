class RepositorioProcesos:
    def __init__(self):
        self.procesos = {}

    def agregar(self, proceso):
        if proceso.pid in self.procesos:
            raise ValueError("Ya existe un proceso con ese PID.")
        self.procesos[proceso.pid] = proceso

    def listar(self):
        return list(self.procesos.values())

    def eliminar(self, pid):
        if pid in self.procesos:
            del self.procesos[pid]
        else:
            raise ValueError("No existe proceso con ese PID.")

    def obtener(self, pid):
        if pid not in self.procesos:
            raise ValueError("Proceso no encontrado.")
        return self.procesos[pid]