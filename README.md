# Laboratorio 11 - Algoritmos Minimax y Poda Alfa-Beta

Este laboratorio implementa Minimax y Poda Alfa-Beta para comparar su
comportamiento en arboles de decision. El objetivo es comprobar que ambos
algoritmos obtienen el mismo valor final, pero Alfa-Beta puede evaluar menos
nodos cuando logra descartar ramas innecesarias.

Tambien se incluye una version sencilla del juego Tres en Raya, donde el agente
usa Poda Alfa-Beta para elegir su mejor movimiento.

## Requisitos

- Python 3.12 o superior
- pip

## Instalacion

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Si PowerShell permite activar scripts:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecucion

```powershell
python -m src.main
```

Para jugar Tres en Raya desde consola:

```powershell
python -m src.main --play
```

## Pruebas

```powershell
pytest
pytest --cov=src --cov-report=term-missing --cov-report=xml
```

## Organizacion del proyecto

```text
src/
  alpha_beta.py
  game_tree.py
  main.py
  minimax.py
  tic_tac_toe.py
tests/
  test_algorithms.py
  test_main.py
  test_tic_tac_toe.py
```

## Comparacion entre Minimax y Poda Alfa-Beta

Minimax revisa todas las hojas del arbol para encontrar la mejor decision bajo
el supuesto de que MAX y MIN juegan racionalmente. Poda Alfa-Beta mantiene la
misma decision final, pero evita recorrer ramas que ya no pueden modificar el
resultado.

El orden de exploracion influye directamente en el rendimiento. Si las mejores
jugadas se encuentran temprano, los limites `alpha` y `beta` se actualizan antes
y el algoritmo puede podar mas ramas. Si las mejores opciones aparecen tarde, el
ahorro es menor y Alfa-Beta se parece mas a Minimax en cantidad de exploracion.

## Tres en Raya

El modulo `src/tic_tac_toe.py` representa el tablero como una tupla de 9
posiciones. El jugador humano usa `X`, el agente usa `O` y las casillas vacias
indican movimientos disponibles.

La funcion `choose_best_move` evalua las jugadas posibles usando Poda Alfa-Beta y
devuelve la mejor casilla para el agente. El modo `--play` permite probarlo como
un juego basico desde consola.

## Observacion tecnica

Durante el desarrollo se identifico una inconsistencia en los valores esperados
del enunciado. Con turnos alternados desde MAX, los valores reales son:
`sample_tree = 3`, `medium_tree = 7` y `ordered_tree = 8`. Por eso las pruebas se
ajustaron para validar el resultado correcto de Minimax.

## Preguntas de analisis

1. Alfa-Beta produce el mismo resultado que Minimax porque solo elimina ramas que
   no pueden cambiar la decision final.
2. `alpha` representa el mejor valor encontrado hasta el momento para MAX.
3. `beta` representa el mejor valor encontrado hasta el momento para MIN.
4. Alfa-Beta ahorra mas trabajo cuando las mejores jugadas aparecen primero.
5. El orden importa porque valores utiles tempranos permiten cerrar antes los
   limites `alpha` y `beta`.
6. Si el rival no juega racionalmente, Minimax puede tomar decisiones demasiado
   conservadoras.
7. En motores de ajedrez, este enfoque ayuda a evaluar jugadas futuras y cortar
   lineas poco prometedoras.
8. Frente a redes neuronales o aprendizaje por refuerzo, este enfoque necesita
   explorar explicitamente el arbol y puede crecer mucho en juegos complejos.
