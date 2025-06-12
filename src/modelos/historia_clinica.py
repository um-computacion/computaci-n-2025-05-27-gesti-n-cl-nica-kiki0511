from src.modelos.paciente import Paciente
from src.modelos.turno import Turno
from src.modelos.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        if not paciente:
            raise ValueError("El paciente es obligatorio.")
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno: Turno):
        if not isinstance(turno, Turno):
            raise TypeError("Debe agregar un objeto Turno.")
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        if not isinstance(receta, Receta):
            raise TypeError("Debe agregar un objeto Receta.")
        self.__recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return list(self.__turnos)  # copia defensiva

    def obtener_recetas(self) -> list[Receta]:
        return list(self.__recetas)

    def __str__(self) -> str:
        texto = f"Historia clínica de {self.__paciente}:\n\n"
        texto += "--- Turnos ---\n"
        if self.__turnos:
            texto += "\n".join(str(t) for t in self.__turnos)
        else:
            texto += "Sin turnos registrados."
        texto += "\n\n--- Recetas ---\n"
        if self.__recetas:
            texto += "\n".join(str(r) for r in self.__recetas)
        else:
            texto += "Sin recetas registradas."
        return texto
