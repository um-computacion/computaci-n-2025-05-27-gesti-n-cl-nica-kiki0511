import unittest
from datetime import datetime
from src.modelos.clinica import Clinica
from src.modelos.paciente import Paciente
from src.modelos.medico import Medico
from src.modelos.especialidad import Especialidad
from src.modelos.excepciones import *

class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Carla Díaz", "12345678", "10/10/1980")
        self.medico = Medico("Dr. Bruno Torres", "M1111")
        self.especialidad = Especialidad("Clínica Médica", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente_y_medico_exitoso(self):
        self.assertEqual(len(self.clinica.obtener_pacientes()), 1)
        self.assertEqual(len(self.clinica.obtener_medicos()), 1)

    def test_error_paciente_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(self.paciente)

    def test_error_medico_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(self.medico)

    def test_obtener_medico_por_matricula_existe(self):
        m = self.clinica.obtener_medico_por_matricula("M1111")
        self.assertIsInstance(m, Medico)
        self.assertEqual(m.obtener_matricula(), "M1111")

    def test_error_obtener_medico_no_existe(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_medico_por_matricula("MX999")

    def test_agendar_turno_correcto(self):
        fecha = datetime(2025, 6, 9, 10, 0)  # lunes
        self.clinica.agendar_turno("12345678", "M1111", "Clínica Médica", fecha)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)

    def test_error_turno_duplicado(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        self.clinica.agendar_turno("12345678", "M1111", "Clínica Médica", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "M1111", "Clínica Médica", fecha)

    def test_error_especialidad_no_disponible_ese_dia(self):
        # Miércoles es válido, volvemos a agendar para probar luego martes
        fecha_ok = datetime(2025, 6, 11, 10, 0)
        self.clinica.agendar_turno("12345678", "M1111", "Clínica Médica", fecha_ok)
        # martes no está en ['lunes','miércoles']
        fecha_mal = datetime(2025, 6, 10, 11, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M1111", "Clínica Médica", fecha_mal)

    def test_agregar_turno_especialidad_incorrecta(self):
        # Intentar agendar con especialidad que el médico no tiene
        fecha = datetime(2025, 6, 9, 12, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M1111", "Pediatría", fecha)

    def test_obtener_historia_clinica_vacia(self):
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(historia.obtener_turnos(), [])
        self.assertEqual(historia.obtener_recetas(), [])

    def test_emitir_receta_correcta(self):
        self.clinica.emitir_receta("12345678", "M1111", ["Ibuprofeno"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_error_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "M1111", [])

    def test_error_emitir_receta_paciente_no_existente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("00000000", "M1111", ["Aspirina"])

    def test_error_turno_medico_no_existente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M9999", "Clínica Médica", datetime(2025, 6, 9, 10, 0))

    def test_error_turno_paciente_no_existente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("00000000", "M1111", "Clínica Médica", datetime(2025, 6, 9, 10, 0))

if __name__ == '__main__':
    unittest.main()
