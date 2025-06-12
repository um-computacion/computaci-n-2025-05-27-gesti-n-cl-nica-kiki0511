import unittest
from src.modelos.paciente import Paciente

class TestPaciente(unittest.TestCase):

    def test_creacion_paciente_valido(self):
        paciente = Paciente("Juan Pérez", "12345678", "01/01/2000")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertIn("Juan Pérez", str(paciente))

    def test_error_por_campos_vacios(self):
        with self.assertRaises(ValueError):
            Paciente("", "12345678", "01/01/2000")
        with self.assertRaises(ValueError):
            Paciente("Juan Pérez", "", "01/01/2000")
        with self.assertRaises(ValueError):
            Paciente("Juan Pérez", "12345678", "")
   
   