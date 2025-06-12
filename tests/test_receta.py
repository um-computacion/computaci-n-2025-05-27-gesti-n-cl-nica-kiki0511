import unittest
from datetime import datetime
from src.modelos.receta import Receta
from src.modelos.paciente import Paciente
from src.modelos.medico import Medico

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Lucía Castro", "33445566", "02/02/1990")
        self.medico = Medico("Dr. Esteban Ruiz", "M9999")

    def test_creacion_receta_valida(self):
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        receta = Receta(self.paciente, self.medico, medicamentos)
        self.assertIn("Paracetamol", str(receta))
        self.assertIn("Lucía Castro", str(receta))
        self.assertIn("Dr. Esteban Ruiz", str(receta))

    def test_error_por_medicamentos_vacios(self):
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])

    def test_error_por_medicamentos_no_lista(self):
        with self.assertRaises(TypeError):
            Receta(self.paciente, self.medico, "Paracetamol")

    def test_error_por_paciente_o_medico_faltante(self):
        medicamentos = ["Amoxicilina"]
        with self.assertRaises(ValueError):
            Receta(None, self.medico, medicamentos)
        with self.assertRaises(ValueError):
            Receta(self.paciente, None, medicamentos)

if __name__ == '__main__':
    unittest.main()
