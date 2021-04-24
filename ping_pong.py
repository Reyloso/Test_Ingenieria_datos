"""
Partida de Ping Pong (OBLIGATORIO) Ana, José y Juan, se fueron una tarde a jugar ping-pong, cada uno jugó la siguiente
cantidad de partidos. Cada que un jugador pierde una partida arranca otra con el jugador en
espera. Ejemplo: Ana vs Juan (Ana gana) - juega (Ana vs Juan), el ganador siempre juega
contra el jugador que está en espera y así sucesivamente hasta completar el número de partidas que se muestran a continuación.
JUGADOR PARTIDOS JUGADOS
    Ana 17
    José 15
    Juan 10
"""

#librerias
import json

#total juegos 
total_games_played = 21

#jugadores
ana = {'name': 'Ana', 'matchs': 0}
jose = {'name': 'Jose', 'matchs': 0}
juan = {'name': 'Juan', 'matchs': 0}

matches = []
    
def run():
    """ funcion para realizar la simulacion de los partidos"""

    # assign order player
    jugador_1 = ana
    jugador_2 = jose
    en_espera = juan

    #iteracion en el rango de 21 juegos
    for i in range(total_games_played):
        # el siguiente condicional si es  en el desarrollo del ejercicio llegue a la conclusión de que habia que colocar a perder a ana en algun momento
        # para asi poder lograr que jose completara sus 15 partidos y juan a 10
        if i != 12:
            # el jugador_1 gana  pero ambos suman un partido
            jugador_1['matchs'] +=1
            jugador_2['matchs'] +=1
            matches.append({'winner':jugador_1['name'], 'loser':jugador_2['name']})
            # se reordenan los jugadores mediante el metodo de la burbuja para que el jugador en espera juegue en la siguiente ronda(iteracion)
            temporal = jugador_2
            jugador_2 = en_espera
            en_espera = temporal
        else:
            # si es en partido numero 12 el jugador 1 pierde pero suma un partido junto al jugador 2
            jugador_1['matchs'] += 1
            jugador_2['matchs'] += 1
            matches.append({'winner':jugador_2['name'], 'loser':jugador_1['name']})

            # se reordenan los jugadores mediante el metodo de la burbuja para que el jugador en espera juegue en la siguiente ronda(iteracion)
            temporal = jugador_1
            temporal2 = jugador_2

            jugador_2 = en_espera
            jugador_1 = temporal2
            en_espera = temporal
            
    print(jugador_1)
    print(jugador_2)
    print(en_espera)
    players = {"jugador_1":jugador_1,"jugador_2":jugador_2,"jugador_3":en_espera}
    data = {"segundo_perdedor":matches[1]['loser'], "jugadores":players, "matches":matches}
    # se retorna la data en formato json
    data = json.dumps(data)
    print(data)

        
run()
    
