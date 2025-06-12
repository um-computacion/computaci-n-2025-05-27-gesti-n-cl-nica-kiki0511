from datetime import datetime
from src.modelos.clinica import Clinica
from src.modelos.paciente import Paciente
from src.modelos.medico import Medico
from src.modelos.especialidad import Especialidad
from src.modelos.excepciones import *

def mostrar_menu():
    print("\n--- Menú Clínica ---")
    print("1) Agregar paciente")
    print("2) Agregar médico")
    print("3) Agendar turno")
    print("4) Agregar especialidad a médico")
    print("5) Emitir receta")
    print("6) Ver historia clínica")
    print("7) Ver todos los turnos")
    print("8) Ver todos los pacientes")
    print("9) Ver todos los médicos")
    print("0) Salir")

def main():
    clinica = Clinica()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del paciente: ")
                dni = input("DNI: ")
                fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
                paciente = Paciente(nombre, dni, fecha_nac)
                clinica.agregar_paciente(paciente)
                print("Paciente agregado correctamente.")

            elif opcion == "2":
                nombre = input("Nombre del médico: ")
                matricula = input("Matrícula: ")
                medico = Medico(nombre, matricula)
                clinica.agregar_medico(medico)
                print("Médico agregado correctamente.")

            elif opcion == "3":
                dni = input("DNI del paciente: ")
                matricula = input("Matrícula del médico: ")
                especialidad = input("Especialidad: ")
                fecha_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
                fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
                clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
                print("Turno agendado correctamente.")

            elif opcion == "4":
                matricula = input("Matrícula del médico: ")
                tipo = input("Nombre de la especialidad: ")
                dias = input("Días de atención (separados por coma): ").split(",")
                dias = [d.strip().lower() for d in dias]
                especialidad = Especialidad(tipo, dias)
                medico = clinica.obtener_medico_por_matricula(matricula)
                medico.agregar_especialidad(especialidad)
                print("Especialidad agregada al médico.")

            elif opcion == "5":
                dni = input("DNI del paciente: ")
                matricula = input("Matrícula del médico: ")
                medicamentos = input("Medicamentos (separados por coma): ").split(",")
                medicamentos = [m.strip() for m in medicamentos]
                clinica.emitir_receta(dni, matricula, medicamentos)
                print("Receta emitida correctamente.")

            elif opcion == "6":
                dni = input("DNI del paciente: ")
                historia = clinica.obtener_historia_clinica(dni)
                print(historia)

            elif opcion == "7":
                turnos = clinica.obtener_turnos()
                if not turnos:
                    print("No hay turnos registrados.")
                for turno in turnos:
                    print(turno)

            elif opcion == "8":
                pacientes = clinica.obtener_pacientes()
                if not pacientes:
                    print("No hay pacientes registrados.")
                for paciente in pacientes:
                    print(paciente)

            elif opcion == "9":
                medicos = clinica.obtener_medicos()
                if not medicos:
                    print("No hay médicos registrados.")
                for medico in medicos:
                    print(medico)

            elif opcion == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except Exception as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()
