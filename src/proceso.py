class Proceso:
    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("PID no puede estar vacío.")
        if duracion <= 0:
            raise ValueError("Duración debe ser un entero positivo.")
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None