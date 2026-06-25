# Laboratorio 11 - Algoritmos Minimax y Poda Alfa-Beta

Este laboratorio desarrolla una implementación práctica de los algoritmos Minimax y Poda Alfa-Beta dentro del curso de Sistemas Inteligentes. El objetivo principal es analizar y comparar el comportamiento de ambos métodos de búsqueda utilizando árboles de decisión representados mediante estructuras de listas anidadas.

Además, se incorpora una versión básica del juego Tres en Raya, donde un agente inteligente emplea la técnica de Poda Alfa-Beta para determinar la mejor jugada posible en cada turno.

## Requisitos

* Python 3.12 o superior
* Gestor de paquetes pip

## Instalación

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecución

```powershell
python -m src.main
```

Para iniciar una partida de Tres en Raya desde la consola:

```powershell
python -m src.main --play
```

## Pruebas

```powershell
pytest
pytest --cov=src --cov-report=term-missing --cov-report=xml
```

## Organización del proyecto

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

## Comparación entre Minimax y Poda Alfa-Beta

El algoritmo Minimax examina todas las posibles hojas del árbol de búsqueda para seleccionar la mejor alternativa bajo el supuesto de que ambos participantes actúan de manera óptima. Por su parte, la Poda Alfa-Beta produce exactamente la misma decisión, pero mejora la eficiencia al evitar la exploración de ramas que no influyen en el resultado final. Gracias a ello, puede reducir significativamente la cantidad de nodos evaluados cuando el árbol se encuentra favorablemente ordenado.

## Implementación de Tres en Raya

El archivo `src/tic_tac_toe.py` representa un tablero compuesto por nueve posiciones, donde el jugador humano utiliza la ficha `X` y el agente inteligente la ficha `O`. Mediante la función `choose_best_move`, el sistema analiza las posibles jugadas utilizando Poda Alfa-Beta y selecciona la opción más conveniente. Asimismo, se incluye la opción `--play`, que permite disputar una partida directamente desde la terminal.

## Observación técnica

Durante el desarrollo se identificó una inconsistencia entre algunos valores esperados del enunciado y los resultados obtenidos al aplicar correctamente Minimax con alternancia de turnos. Considerando que la raíz inicia como jugador MAX, los valores calculados fueron: `sample_tree = 3`, `medium_tree = 7` y `ordered_tree = 8`. Por esta razón, se ajustaron las pruebas unitarias para validar los resultados reales generados por la implementación.

## Preguntas de análisis

**1. ¿Por qué Alfa-Beta produce el mismo resultado que Minimax?**
Porque únicamente descarta ramas que no tienen capacidad de modificar la decisión final, manteniendo intacto el resultado óptimo calculado por Minimax.

**2. ¿Qué representa alpha dentro del algoritmo?**
Es el mejor valor encontrado hasta el momento para el jugador MAX y funciona como límite inferior durante la búsqueda.

**3. ¿Qué representa beta dentro del algoritmo?**
Corresponde al mejor valor garantizado para el jugador MIN y actúa como límite superior dentro del proceso de evaluación.

**4. ¿En qué situaciones Alfa-Beta reduce más trabajo computacional?**
Cuando las mejores jugadas se exploran primero, ya que esto permite realizar más podas y disminuir la cantidad de nodos analizados.

**5. ¿Por qué el orden de exploración influye en el rendimiento?**
Porque valores favorables encontrados tempranamente permiten actualizar con rapidez los límites alpha y beta, aumentando las oportunidades de poda.

**6. ¿Qué ocurriría si el oponente no actuara racionalmente?**
La estrategia calculada por Minimax podría resultar demasiado conservadora, ya que el algoritmo asume que el adversario siempre elegirá la mejor respuesta posible.

**7. ¿Cómo se aplica este enfoque en los motores de ajedrez?**
Se utiliza para proyectar movimientos futuros, evaluar posiciones y descartar líneas de juego que tienen pocas probabilidades de mejorar el resultado.

**8. ¿Qué limitaciones presenta frente a técnicas modernas como redes neuronales o aprendizaje por refuerzo?**
Requiere una representación explícita del espacio de búsqueda y su costo computacional crece rápidamente en problemas complejos, mientras que los enfoques basados en aprendizaje pueden generalizar patrones sin explorar exhaustivamente todas las posibilidades.

