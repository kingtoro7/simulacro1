class Jugador:
    def __init__(self, nombre, apellidos, dorsal, altura, peso):
        self.nombre = nombre    #Damos de alta las 3 clases que nos piden
        self.apellidos = apellidos
        self.dorsal = dorsal
        self.altura = altura
        self.peso = peso

class Entrenador:
    def __init__(self, nombre, apellidos, año_licencia):
        self.nombre = nombre
        self.apellidos = apellidos
        self.año_licencia = año_licencia

class Equipo:
    def __init__(self, nombre, ciudad, entrenador):
        self.nombre = nombre
        self.ciudad = ciudad
        self.entrenador = entrenador
        self.jugadores = []

    def alta_jugador(self, jugador):
        self.jugadores.append(jugador)

    def baja_jugador(self, jugador):
        self.jugadores.remove(jugador)

    def lista_jugadores_mas_altos(self):
        if not self.jugadores:  #Pregunta si hay jugadores en el equipo, en caso de no, suelta el print.
            print("No hay jugadores en este equipo.")
            return []
        jugadores_altos = sorted(self.jugadores, key=lambda jugador: jugador.altura, reverse=True)
        return jugadores_altos  #Si hay jugadores, procede a ordenarlos por altura, la funcion sorted es para ordenar
                                #La clave de ordenamiento se especifica mediante el parámetro key, 
                                #que utiliza una función lambda para obtener la altura de cada jugador. 
                                #El parámetro reverse=True indica que la lista se ordenará de mayor a menor altura.

class Liga:
    def __init__(self):
        self.equipos = []

    def alta_equipo(self, equipo):
        self.equipos.append(equipo)

    def baja_equipo(self, nombre_equipo):
        for equipo in self.equipos:
            if equipo.nombre == nombre_equipo:
                self.equipos.remove(equipo)
                print(f"El equipo {nombre_equipo} ha sido dado de baja.")
                return
        print(f"No se encontró ningún equipo con el nombre {nombre_equipo}.")

    def lista_entrenadores_ordenados(self):
        if not self.equipos:
            print("No hay equipos registrados en la liga.")
            return []
        entrenadores = []
        for equipo in self.equipos:
            entrenadores.append(equipo.entrenador)
        entrenadores_ordenados = sorted(entrenadores, key=lambda entrenador: entrenador.año_licencia)
        return entrenadores_ordenados   #Ordenar los entrenadores, con el array

liga = Liga()

equipo1_entrenador = Entrenador("Juan", "Pérez", 2000)
equipo1 = Equipo("Equipo A", "Ciudad A", equipo1_entrenador)
equipo1.alta_jugador(Jugador("Carlos", "González", 10, 180, 80))
equipo1.alta_jugador(Jugador("Luis", "Martínez", 7, 190, 85))
equipo1.alta_jugador(Jugador("Ana", "Sánchez", 14, 170, 65))
liga.alta_equipo(equipo1)

equipo2_entrenador = Entrenador("Pedro", "López", 2010)
equipo2 = Equipo("Equipo B", "Ciudad B", equipo2_entrenador)
equipo2.alta_jugador(Jugador("María", "Gómez", 9, 185, 75))
equipo2.alta_jugador(Jugador("Sergio", "Ruiz", 5, 195, 90))
equipo2.alta_jugador(Jugador("Laura", "Fernández", 12, 175, 70))
liga.alta_equipo(equipo2)

# Lista de jugadores más altos por equipo
print("Jugadores más altos por equipo:")
for equipo in liga.equipos:
    print(f"Equipo: {equipo.nombre}")
    jugadores_altos = equipo.lista_jugadores_mas_altos()
    for jugador in jugadores_altos:
        print(f"- {jugador.nombre} {jugador.apellidos} ({jugador.altura} cm)")

# Lista de entrenadores ordenados por año de licencia
print("\nEntrenadores ordenados por año de licencia:")
entrenadores_ordenados = liga.lista_entrenadores_ordenados()
for entrenador in entrenadores_ordenados:
    print(f"{entrenador.nombre} {entrenador.apellidos} - Año de licencia: {entrenador.año_licencia}")
