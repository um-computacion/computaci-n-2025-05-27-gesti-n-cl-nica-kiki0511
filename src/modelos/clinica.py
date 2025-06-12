from datetime import datetime
from src.modelos.paciente import Paciente
from src.modelos.medico import Medico
from src.modelos.turno import Turno
from src.modelos.receta import Receta
from src.modelos.historia_clinica import HistoriaClinica
from src.modelos.excepciones import *

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}

    # ------------------ Registro y Acceso ------------------

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError("Ya existe un paciente con ese DNI.")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError("Ya existe un médico con esa matrícula.")
        self.__medicos[matricula] = medico

    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        if matricula not in self.__medicos:
            raise PacienteNoEncontradoException("Médico no encontrado.")
        return self.__medicos[matricula]

    # ------------------ Turnos ------------------

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)

        medico = self.__medicos[matricula]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)

        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)

        turno = Turno(self.__pacientes[dni], medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def obtener_turnos(self) -> list[Turno]:
        return list(self.__turnos)

    # ------------------ Recetas ------------------

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        if not medicamentos:
            raise RecetaInvalidaException("La receta debe tener al menos un medicamento.")

        receta = Receta(self.__pacientes[dni], self.__medicos[matricula], medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]

    # ------------------ Validaciones ------------------

    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"Paciente con DNI {dni} no encontrado.")

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException(f"Médico con matrícula {matricula} no encontrado.")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException("Ya hay un turno asignado con ese médico en ese horario.")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str | None:
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        especialidad_disponible = self.obtener_especialidad_disponible(medico, dia_semana)
        if especialidad_disponible is None or especialidad_disponible.lower() != especialidad_solicitada.lower():
            raise MedicoNoDisponibleException("El médico no atiende esa especialidad en ese día.")
