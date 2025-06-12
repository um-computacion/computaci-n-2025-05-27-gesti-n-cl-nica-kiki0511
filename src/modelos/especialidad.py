class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        if not tipo or not dias:
            raise ValueError("La especialidad y los días no pueden estar vacíos.")
        if not all(isinstance(d, str) for d in dias):
            raise TypeError("Todos los días deben ser cadenas de texto.")
        self.__tipo = tipo
        self.__dias = [d.lower() for d in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ', '.join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"
##3
    def __init__(self, tipo: str, dias: list[str]):
        if not tipo or not dias:
            raise ValueError("La especialidad y los días no pueden estar vacíos.")
        if not all(isinstance(d, str) for d in dias):
            raise TypeError("Todos los días deben ser cadenas de texto.")
        self.__tipo = tipo
        self.__dias = [d.strip().lower() for d in dias]
