# tp12.py
# Trabajo Práctico 12 - POO
# Implementación de ejemplos solicitados

class Curso:
    def __init__(self, nombre, nivel, docente):
        self.nombre = nombre        # atributo 1
        self.nivel = nivel          # atributo 2
        self.docente = docente      # atributo 3
        self.alumnos = []           # atributo adicional (lista)

    def iniciar_clase(self):
        print(f"Se inicia la clase de {self.nombre} ({self.nivel}) con {self.docente}.")

    def terminar_trimestre(self):
        print(f"Se terminó el trimestre de {self.nombre}. Lista de alumnos: {self.alumnos}")

    def agregar_alumno(self, nombre_alumno):
        self.alumnos.append(nombre_alumno)


class Computadora:
    def __init__(self, marca, ram_gb, estado=False):
        self.marca = marca          # atributo 1
        self.ram_gb = ram_gb        # atributo 2
        self.encendida = estado     # atributo 3 (estado booleano)
        self.programas = []         # lista de programas instalados

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print(f"{self.marca} encendida.")
        else:
            print(f"{self.marca} ya está encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print(f"{self.marca} apagada.")
        else:
            print(f"{self.marca} ya está apagada.")

    def instalar_programa(self, nombre_programa):
        self.programas.append(nombre_programa)
        print(f"Instalado: {nombre_programa}")


class TelefonoMovil:
    def __init__(self, bateria_pct, so, numero):
        self.bateria_pct = bateria_pct  # atributo 1
        self.sistema_operativo = so     # atributo 2
        self.numero = numero            # atributo 3
        self.mensajes = []              # lista de mensajes

    def llamar(self, destino):
        print(f"Llamando desde {self.numero} a {destino}...")

    def enviar_mensaje(self, destino, texto):
        mensaje = {"origen": self.numero, "destino": destino, "texto": texto}
        self.mensajes.append(mensaje)
        print(f"Mensaje enviado a {destino}: {texto}")

    def cargar(self, cantidad):
        self.bateria_pct = min(100, self.bateria_pct + cantidad)
        print(f"Batería: {self.bateria_pct}%")


class Profesor:
    def __init__(self, nombre, materia, antiguedad):
        self.nombre = nombre
        self.materia = materia
        self.antiguedad = antiguedad
        self.trabajos_calificados = []  # lista que registra calificaciones

    def dar_clase(self):
        print(f"{self.nombre} está dando clase de {self.materia}.")

    def calificar_trabajo(self, alumno, nota):
        self.trabajos_calificados.append({"alumno": alumno, "nota": nota})
        print(f"{self.nombre} calificó a {alumno} con {nota}.")


class Cancion:
    def __init__(self, titulo, artista, duracion_seg):
        self.titulo = titulo
        self.artista = artista
        self.duracion_seg = duracion_seg
        self.estado = "detenida"  # puede ser "reproduciendo", "pausada", "detenida"

    def reproducir(self):
        self.estado = "reproduciendo"
        print(f"Reproduciendo: {self.titulo} - {self.artista}")

    def pausar(self):
        if self.estado == "reproduciendo":
            self.estado = "pausada"
            print(f"Pausado: {self.titulo}")
        else:
            print("No se puede pausar si no está reproduciendo.")


# II. Listas como atributos (se ma
