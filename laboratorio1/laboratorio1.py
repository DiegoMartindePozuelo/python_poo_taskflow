class Tarea:
    def __init__(self, titulo: str, responsable=None):
        self.titulo = titulo
        self.estado = "pendiente"   # estado inicial
        self.responsable = responsable

    def iniciar(self) -> None:
        if self.estado == "pendiente":
            self.estado = "en progreso"

    def completar(self) -> None:
        if self.estado == "en progreso":
            self.estado = "completada"

    def reasignar(self, nuevo_responsable) -> None:
        self.responsable = nuevo_responsable

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.tareas_asignadas = []

    def registrarse(self) -> None:
        # En un sistema real esto haría más cosas,
        # pero en el modelo conceptual basta con que exista el método.
        print(f"Usuario {self.nombre} registrado.")

    def consultar_tareas(self) -> None:
        if not self.tareas_asignadas:
            print(f"{self.nombre} no tiene tareas asignadas.")
            return

        print(f"Tareas asignadas a {self.nombre}:")
        for tarea in self.tareas_asignadas:
            print(f"- {tarea.titulo} ({tarea.estado})")

    def recibir_tarea(self, tarea) -> None:
        self.tareas_asignadas.append(tarea)

class Proyecto:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.tareas = []

    def crear_tarea(self, titulo: str, responsable=None) -> Tarea:
        nueva_tarea = Tarea(titulo, responsable)
        self.tareas.append(nueva_tarea)
        return nueva_tarea

    def añadir_tarea(self, tarea: Tarea) -> None:
        self.tareas.append(tarea)

    def listar_tareas(self) -> None:
        if not self.tareas:
            print(f"El proyecto '{self.nombre}' no tiene tareas.")
            return

        print(f"Tareas del proyecto '{self.nombre}':")
        for tarea in self.tareas:
            responsable = tarea.responsable.nombre if tarea.responsable else "Sin responsable"
            print(f"- {tarea.titulo} ({tarea.estado}) — Responsable: {responsable}")
