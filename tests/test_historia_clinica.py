import unittest
from datetime import datetime
from src.modelos.paciente import Paciente
from src.modelos.medico import Medico
from src.modelos.turno import Turno
from src.modelos.receta import Receta
from src.modelos.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Julián Gómez", "99887766", "20/09/1995")
        self.medico = Medico("Dr. Ramiro Díaz", "M5555")
        self.turno = Turno(self.paciente, self.medico, datetime(2025, 6, 12, 10, 0), "Clínica Médica")
        self.receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_y_obtener_turno(self):
        self.historia.agregar_turno(self.turno)
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0], self.turno)

    def test_agregar_y_obtener_receta(self):
        self.historia.agregar_receta(self.receta)
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0], self.receta)

    def test_representacion_str(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        texto = str(self.historia)
        self.assertIn("Historia clínica", texto)
        self.assertIn("Turno de", texto)
        self.assertIn("Receta para", texto)

    def test_errores_por_objetos_invalidos(self):
        with self.assertRaises(TypeError):
            self.historia.agregar_turno("no es un turno")
        with self.assertRaises(TypeError):
            self.historia.agregar_receta(123)

    def test_error_por_paciente_none(self):
        with self.assertRaises(ValueError):
            HistoriaClinica(None)

if __name__ == '__main__':
    unittest.main()
