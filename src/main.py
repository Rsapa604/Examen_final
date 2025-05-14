from src.proceso import Proceso
from src.repositorio import RepositorioProcesos
from src.scheduler import FCFSScheduler, RoundRobinScheduler
from src.metrics import calcular_metricas

repo = RepositorioProcesos()

def menu():
    print("\n--- Gestor de Procesos ---")
    print("1. Agregar proceso")
    print("2. Listar procesos")
    print("3. Eliminar proceso")
    print("4. Guardar JSON")
    print("5. Cargar JSON")
    print("6. Ejecutar FCFS")
    print("7. Ejecutar Round-Robin")
    print("0. Salir")

while True:
    menu()
    op = input("Opción: ")

    if op == "1":
        pid = input("PID: ")
        dur = int(input("Duración: "))
        pri = int(input("Prioridad: "))
        repo.agregar(Proceso(pid, dur, pri))
    elif op == "2":
        for p in repo.listar():
            print(p)
    elif op == "3":
        pid = input("PID a eliminar: ")
        repo.eliminar(pid)
    elif op == "4":
        ruta = input("Ruta JSON: ")
        repo.guardar_json(ruta)
    elif op == "5":
        ruta = input("Ruta JSON: ")
        repo.cargar_json(ruta)
    elif op == "6":
        procesos = repo.listar()
        s = FCFSScheduler()
        gantt = s.planificar(procesos)
        for g in gantt:
            print(f"{g[0]}: {g[1]} → {g[2]}")
        print(calcular_metricas(procesos))
    elif op == "7":
        q = int(input("Quantum: "))
        procesos = repo.listar()
        s = RoundRobinScheduler(q)
        gantt = s.planificar(procesos)
        for g in gantt:
            print(f"{g[0]}: {g[1]} → {g[2]}")
        print(calcular_metricas(procesos))
    elif op == "0":
        break
    else:
        print("Opción inválida.")