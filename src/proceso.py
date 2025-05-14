class Proceso:
    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("PID no puede estar vacío.")
        if duracion <= 0:
            raise ValueError("Duración debe ser un entero positivo.")