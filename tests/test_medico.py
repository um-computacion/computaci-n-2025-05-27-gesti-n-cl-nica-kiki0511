import unittest
from src.modelos.medico import Medico
from src.modelos.especialidad import Especialidad

class TestMedico(unittest.TestCase):

    def test_creacion_medico_valido(self):
        medico = Medico("Ana García", "M1234")
        self.assertEqual(medico.obtener_matricula(), "M1234")
        self.assertIn("Ana García", str(medico))

    def test_error_por_datos_vacios(self):
        with self.assertRaises(ValueError):
            Medico("", "M1234")
        with self.assertRaises(ValueError):
            Medico("Ana García", "")

    def test_agregar_especialidad_valida(self):
        medico = Medico("Carlos López", "M5678")
        esp = Especialidad("Pediatría", ["lunes", "miércoles"])
        medico.agregar_especialidad(esp)
        self.assertIn("Pediatría", str(medico))

    def test_obtener_especialidad_para_dia(self):
        medico = Medico("Laura Pérez", "M9012")
        esp1 = Especialidad("Cardiología", ["martes", "jueves"])
        esp2 = Especialidad("Clínica Médica", ["lunes"])
        medico.agregar_especialidad(esp1)
        medico.agregar_especialidad(esp2)
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), "Cardiología")
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Clínica Médica")
        self.assertIsNone(medico.obtener_especialidad_para_dia("domingo"))

    def test_error_al_agregar_especialidad_invalida(self):
        medico = Medico("Federico Gómez", "M8888")
        with self.assertRaises(TypeError):
            medico.agregar_especialidad("No es una especialidad")

if __name__ == '__main__':
    unittest.main()
