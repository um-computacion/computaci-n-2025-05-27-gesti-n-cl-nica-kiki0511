import unittest
from datetime import datetime
from src.modelos.turno import Turno
from src.modelos.paciente import Paciente
from src.modelos.medico import Medico

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("María López", "11222333", "15/05/1985")
        self.medico = Medico("Dr. Alberto Pérez", "M4455")
        self.fecha_hora = datetime(2025, 6, 10, 14, 30)
        self.especialidad = "Dermatología"

    def test_creacion_turno_valido(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad)
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)
        self.assertIn("María López", str(turno))
        self.assertIn("Dermatología", str(turno))

    def test_error_por_campos_faltantes(self):
        with self.assertRaises(ValueError):
            Turno(None, self.medico, self.fecha_hora, self.especialidad)
        with self.assertRaises(ValueError):
            Turno(self.paciente, None, self.fecha_hora, self.especialidad)
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, None, self.especialidad)
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha_hora, "")

    def test_error_si_fecha_no_es_datetime(self):
        with self.assertRaises(TypeError):
            Turno(self.paciente, self.medico, "10/06/2025 14:30", self.especialidad)
    def test_turnos_distintos_con_misma_fecha_y_datos_son_diferentes_objetos(self):
        turno1 = Turno(self.paciente, self.medico, self.fecha_hora, "Dermatología")
        turno2 = Turno(self.paciente, self.medico, self.fecha_hora, "Clínica Médica")
        self.assertNotEqual(str(turno1), str(turno2))

    def test_turno_str_muestra_fecha_en_formato_correcto(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad)
        self.assertIn("10/06/2025 14:30", str(turno))

    def test_paciente_puede_tener_varios_turnos_distintos(self):
        otra_fecha = datetime(2025, 6, 12, 9, 0)
        turno1 = Turno(self.paciente, self.medico, self.fecha_hora, "Dermatología")
        turno2 = Turno(self.paciente, self.medico, otra_fecha, "Dermatología")
        self.assertNotEqual(turno1.obtener_fecha_hora(), turno2.obtener_fecha_hora())
   
if __name__ == '__main__':
    unittest.main()
