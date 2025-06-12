# 🏥 Sistema de Gestión para una Clínica

## 📋 Datos Personales

* **Nombre y Apellido**: Joaquin Tejada Pareja
* **Ciclo Lectivo**: 2025
* **Carrera**: Ingeneiria en informatica

---

## 🔢 Cómo ejecutar el sistema

1. Asegurarse de tener instalado **Python 3.8 o superior**.
2. Abrir una terminal y ubicarse en la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python3 main.py
```

Esto abrirá el menú principal del sistema, donde el usuario podrá realizar:

* Registro de pacientes y médicos
* Agregado de especialidades a médicos
* Agendamiento de turnos
* Emisión de recetas
* Consulta de historias clínicas
* Visualización de todos los turnos, pacientes y médicos

El sistema permanece en bucle hasta que el usuario selecciona **"0 - Salir"**.

---

## 🧪 Cómo ejecutar las pruebas

1. Desde la carpeta raíz del proyecto, ejecutar:

```bash
python3 -m unittest discover tests
```

Esto ejecuta todos los archivos de prueba ubicados en la carpeta `tests`, validando el correcto funcionamiento del sistema y el manejo de errores.

Los tests cubren:

* Registro de pacientes y médicos (y errores por duplicación)
* Agendamiento de turnos (y errores por disponibilidad o duplicados)
* Emisión de recetas (y errores por listas vacías)
* Historial médico (turnos y recetas)

---

## 🧐 Explicación de diseño general

El sistema está construido utilizando **Programación Orientada a Objetos**, y estructurado en tres grandes módulos:

### 1. Modelo (`src/modelos/`)

Contiene las clases que representan el dominio del problema:

* `Paciente`: contiene nombre, DNI y fecha de nacimiento.
* `Medico`: contiene nombre, matrícula y especialidades.
* `Especialidad`: tipo y días de atención.
* `Turno`: vincula paciente, médico, especialidad y fecha/hora.
* `Receta`: contiene paciente, médico, medicamentos y fecha.
* `HistoriaClinica`: lista de turnos y recetas de cada paciente.
* `Clinica`: clase central que orquesta todas las operaciones del sistema.
* `excepciones.py`: contiene excepciones personalizadas del dominio.

### 2. Interfaz CLI (`src/cli.py`)

* Provee una interfaz de texto amigable para el usuario.
* Pide datos, muestra opciones y resultados.
* Utiliza `try/except` para mostrar mensajes amigables.
* No contiene lógica de negocio: delega todo a la clase `Clinica`.

### 3. Pruebas (`tests/`)

* Utiliza `unittest` para verificar el comportamiento de cada clase.
* Los tests están divididos por archivo (uno por clase).
* Cubre tanto casos exitosos como errores esperables.

---

## ⚠️ Consideraciones técnicas

* Se implementaron **excepciones personalizadas** para casos comunes del dominio (por ejemplo: paciente no encontrado, turno duplicado, receta vacía).
* El archivo `main.py` permite ejecutar el sistema directamente desde la raíz del proyecto sin tener que configurar variables de entorno.
* El sistema está diseñado para ser escalable, permitiendo agregar nuevas funcionalidades sin modificar la estructura actual.
