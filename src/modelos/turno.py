from datetime import datetime
from src.modelos.paciente import Paciente
from src.modelos.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if not all([paciente, medico, fecha_hora, especialidad]):
            raise ValueError("Todos los campos del turno son obligatorios.")
        if not isinstance(fecha_hora, datetime):
            raise TypeError("fecha_hora debe ser un objeto datetime.")
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return (
            f"Turno de {self.__paciente} con {self.__medico} "
            f"por {self.__especialidad} el {self.__fecha_hora.strftime('%d/%m/%Y %H:%M')}"
        )

