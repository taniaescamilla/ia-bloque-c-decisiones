# Bloque C: Toma de Decisiones — Resumen Teorico

## 1. Teoria de decisiones

### Decisiones bajo incertidumbre
Se tiene una matriz de pagos con acciones (filas) y estados de la naturaleza (columnas). Criterios:

- **Maximin (Wald):** elegir la accion cuyo peor caso es el mejor. Pesimista
- **Maximax:** elegir la accion con el mejor resultado posible. Optimista
- **Hurwicz:** ponderacion entre optimismo y pesimismo con parametro alfa
- **Laplace:** asignar probabilidades iguales a todos los estados
- **Minimax regret (Savage):** minimizar el maximo arrepentimiento

### Decisiones bajo riesgo
Se conocen las probabilidades de cada estado. Se usa el **valor esperado**:
- E[accion] = suma de (probabilidad x pago) para cada estado
- **VEIP (Valor Esperado de Informacion Perfecta):** cuanto pagarias por saber el estado con certeza

## 2. Teoria de la utilidad

### Utilidad ordinal vs cardinal
- **Ordinal:** solo permite ranking (A > B > C)
- **Cardinal:** permite comparar magnitudes (cuanto mas prefiero A sobre B)
- **Utilidad esperada:** permite decisiones racionales bajo riesgo

### Axiomas de von Neumann-Morgenstern (1944)
1. **Completitud:** para todo par A, B: A > B, B > A, o A ~ B
2. **Transitividad:** si A > B y B > C, entonces A > C
3. **Continuidad:** si A > B > C, existe p tal que B ~ pA + (1-p)C
4. **Independencia:** si A > B, entonces pA + (1-p)C > pB + (1-p)C

### Aversion al riesgo
- Averso: u(x) concava, prefiere el valor esperado seguro a la loteria
- Neutral: u(x) lineal
- Amante del riesgo: u(x) convexa

### Paradojas
- **San Petersburgo:** demuestra que el dinero no es utilidad (valor esperado infinito, nadie pagaria infinito)
- **Allais (1953):** viola el axioma de independencia. Las personas ponderan la certeza desproporcionadamente
- **Ellsberg (1961):** viola probabilidad subjetiva. Las personas prefieren riesgo conocido sobre ambiguedad

### Prospect Theory (Kahneman & Tversky, 1979)
- Las personas evaluan respecto a un punto de referencia, no en terminos absolutos
- Funcion de valor en S: concava para ganancias, convexa para perdidas
- Aversion a la perdida: lambda ~ 2.25 (perder duele 2.25x mas que ganar)
- Ponderacion de probabilidades: sobreponderar eventos raros, subponderar eventos probables

## 3. Teoria de juegos

### Definicion de juego
- **Jugadores:** agentes que toman decisiones
- **Estrategias:** opciones disponibles para cada jugador
- **Pagos:** resultado para cada combinacion de estrategias

### Juegos de suma cero
Los pagos de todos los jugadores suman cero. Lo que gana uno, lo pierde otro.
Ejemplo: piedra/papel/tijera.

### Estrategia dominante
Una estrategia que es mejor sin importar lo que haga el oponente. Si existe, es la eleccion racional.

### Equilibrio de Nash (1950)
Un perfil de estrategias donde ningun jugador puede mejorar cambiando unilateralmente.
- **Teorema de Nash:** todo juego finito tiene al menos un equilibrio de Nash (posiblemente en estrategias mixtas)
- La demostracion usa el teorema de punto fijo de Kakutani

### Estrategias mixtas
Asignar probabilidades a las estrategias puras. En piedra/papel/tijera, el equilibrio mixto es (1/3, 1/3, 1/3).

### Dilema del prisionero
- Ambos cooperar = mejor resultado colectivo
- Equilibrio de Nash = ambos traicionar (suboptimo socialmente)
- Demuestra tension entre racionalidad individual y bienestar colectivo

## 4. Utilidad multicriterio (MAUT)

### Multi-Attribute Utility Theory (Keeney & Raiffa, 1976)
Para decisiones con multiples objetivos:
- U(x) = suma de w_i * u_i(x_i)
- Requiere independencia preferencial entre atributos
- Los pesos w_i reflejan importancia relativa
- Cada u_i normaliza el atributo a [0,1]

### Arboles de decision
- Nodos de decision (cuadrados): el agente elige
- Nodos de azar (circulos): la naturaleza elige con probabilidades
- Se resuelven por induccion hacia atras (backward induction)

## 5. Conexiones con IA y Ciencia de Datos

- **RLHF:** aprendizaje por refuerzo con feedback humano usa funciones de utilidad para alinear modelos
- **Multi-agent RL:** los agentes aprenden equilibrios de Nash
- **Arboles de decision en ML vs teoria de decisiones:** misma estructura, distinto objetivo
- **Bandits (multi-armed):** balance exploracion/explotacion, fundamento en teoria de decisiones
- **GANs:** juego de suma cero entre generador y discriminador

## Fuentes principales

- von Neumann, J. & Morgenstern, O. (1944). Theory of Games and Economic Behavior.
- Nash, J. (1950). Equilibrium Points in N-Person Games. PNAS.
- Kahneman, D. & Tversky, A. (1979). Prospect Theory. Econometrica.
- Allais, M. (1953). Le comportement de l'homme rationnel devant le risque.
- Luce, R.D. & Raiffa, H. (1957). Games and Decisions.
- Osborne, M.J. & Rubinstein, A. (1994). A Course in Game Theory.
- Keeney, R.L. & Raiffa, H. (1976). Decisions with Multiple Objectives.
- Russell, S. & Norvig, P. (2021). AIMA 4th ed., capitulos 16-17.
