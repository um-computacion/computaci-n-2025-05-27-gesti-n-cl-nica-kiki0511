class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre or not dni or not fecha_nacimiento:
            raise ValueError("Todos los campos son obligatorios.")
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"{self.__nombre} (DNI: {self.__dni}, Fecha de nacimiento: {self.__fecha_nacimiento})"
