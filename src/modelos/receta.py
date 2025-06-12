from datetime import datetime
from src.modelos.paciente import Paciente
from src.modelos.medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not paciente or not medico or not medicamentos:
            raise ValueError("Paciente, médico y lista de medicamentos son obligatorios.")
        if not isinstance(medicamentos, list) or not all(isinstance(med, str) for med in medicamentos):
            raise TypeError("Los medicamentos deben ser una lista de strings.")
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos)
        return (
            f"Receta para {self.__paciente} emitida por {self.__medico} "
            f"el {self.__fecha.strftime('%d/%m/%Y %H:%M')}.\n"
            f"Medicamentos: {medicamentos_str}"
        )

