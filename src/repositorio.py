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
    def guardar_json(self, ruta):
        datos = []
        for p in self.procesos.values():
            datos.append({
                "pid": p.pid,
                "duracion": p.duracion,
                "prioridad": p.prioridad
            })
        with open(ruta, "w") as f:
            import json
            json.dump(datos, f, indent=2)

    def cargar_json(self, ruta):
        with open(ruta, "r") as f:
            import json
            datos = json.load(f)
        self.procesos = {}
        

    def guardar_csv(self, ruta):
        with open(ruta, "w") as f:
            f.write("pid;duracion;prioridad\n")
            for p in self.procesos.values():
                f.write(f"{p.pid};{p.duracion};{p.prioridad}\n")

    def cargar_csv(self, ruta):
        with open(ruta, "r") as f:
            lines = f.readlines()
        self.procesos = {}
        