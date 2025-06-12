from src.modelos.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str):
        if not nombre or not matricula:
            raise ValueError("Nombre y matrícula son obligatorios.")
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = []

    def agregar_especialidad(self, especialidad: Especialidad):
        if not isinstance(especialidad, Especialidad):
            raise TypeError("Debe ser una instancia de Especialidad.")
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for esp in self.__especialidades:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades_str = ', '.join([esp.obtener_especialidad() for esp in self.__especialidades])
        return f"Dr. {self.__nombre} (Matrícula: {self.__matricula}, Especialidades: {especialidades_str})"
