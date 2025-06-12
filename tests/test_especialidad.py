import unittest
from src.modelos.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_creacion_valida_y_str(self):
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.assertEqual(esp.obtener_especialidad(), "Cardiología")
        self.assertIn("lunes", str(esp))
        self.assertIn("miércoles", str(esp))

    def test_verificar_dia_valido_insensible_a_mayusculas(self):
        esp = Especialidad("Dermatología", ["martes"])
        self.assertTrue(esp.verificar_dia("MARTES"))
        self.assertTrue(esp.verificar_dia("martes"))
        self.assertFalse(esp.verificar_dia("jueves"))

    def test_dias_con_espacios_extra(self):
        esp = Especialidad("Neurología", [" lunes ", " miércoles "])
        self.assertTrue(esp.verificar_dia("lunes"))
        self.assertTrue(esp.verificar_dia("miércoles"))

    def test_error_si_dias_no_son_lista_de_str(self):
        with self.assertRaises(TypeError):
            Especialidad("Gastroenterología", [1, 2, 3])

    def test_error_si_tipo_o_dias_vacios(self):
        with self.assertRaises(ValueError):
            Especialidad("", ["lunes"])
        with self.assertRaises(ValueError):
            Especialidad("Pediatría", [])

if __name__ == '__main__':
    unittest.main()
