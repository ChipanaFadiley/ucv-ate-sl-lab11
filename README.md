# Laboratorio 11 - Minimax y Poda Alfa-Beta

Implementacion local del laboratorio de Sistemas Inteligentes. El proyecto
compara el algoritmo Minimax con Poda Alfa-Beta usando arboles de juego
representados como listas anidadas.

Tambien se incluye una version sencilla de tres en raya donde el agente usa
Poda Alfa-Beta para elegir su mejor movimiento.

## Requisitos

- Python 3.12 o superior
- pip

## Instalacion

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecucion

```powershell
python -m src.main
```

Para jugar tres en raya desde consola:

```powershell
python -m src.main --play
```

## Pruebas

```powershell
pytest
pytest --cov=src --cov-report=term-missing --cov-report=xml
```

## Estructura

```text
src/
  alpha_beta.py
  game_tree.py
  main.py
  minimax.py
  tic_tac_toe.py
tests/
  test_algorithms.py
  test_tic_tac_toe.py
```

## Comparacion breve

Minimax evalua todas las hojas del arbol para garantizar la mejor decision
suponiendo que ambos jugadores actuan racionalmente. Alfa-Beta conserva el
mismo resultado, pero descarta ramas que ya no pueden cambiar la decision final.
Por eso puede revisar menos hojas cuando el orden de exploracion es favorable.

## Tres en raya

El modulo `src/tic_tac_toe.py` modela un tablero de 9 casillas con `X` como
jugador humano y `O` como agente. La funcion `choose_best_move` analiza las
jugadas disponibles con Poda Alfa-Beta y devuelve el movimiento recomendado.
Tambien se incluye el modo `--play` para jugar desde consola contra el agente.

## Nota tecnica para screenshot

El error del enunciado esta en los valores esperados: con turnos alternados desde
MAX, `sample_tree` devuelve 3, `medium_tree` devuelve 7 y `ordered_tree` devuelve
8; la solucion fue corregir las pruebas para validar el resultado real de
Minimax.

## Preguntas de analisis

1. Alfa-Beta obtiene el mismo resultado que Minimax porque solo elimina ramas que
   ya no pueden mejorar la decision del jugador actual.
2. `alpha` representa la mejor puntuacion garantizada hasta el momento para MAX.
3. `beta` representa la mejor puntuacion garantizada hasta el momento para MIN.
4. Ahorra mas trabajo cuando los mejores movimientos se exploran primero.
5. El orden afecta el rendimiento porque buenos valores tempranos cierran antes
   los limites `alpha` y `beta`.
6. Si el rival no juega racionalmente, la prediccion de Minimax puede ser
   demasiado conservadora.
7. Los motores de ajedrez usan esta idea para explorar jugadas futuras y cortar
   lineas poco prometedoras.
8. Frente a redes neuronales o aprendizaje por refuerzo, este enfoque depende de
   una evaluacion explicita del arbol y puede crecer demasiado en juegos grandes.
