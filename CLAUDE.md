# CLAUDE.md — Bloque C: Toma de Decisiones

## Proposito de este archivo

Este archivo proporciona contexto al agente de IA (Claude Code) sobre el proyecto. En una clase de Inteligencia Artificial, esto no es solo una conveniencia tecnica sino una demostracion de como se configura un agente con contexto adecuado para que sus outputs sean utiles y verificables.

Un agente sin contexto alucina. Un agente con contexto acotado produce outputs verificables. Este archivo es el mecanismo de acotacion.

## Contexto del proyecto

- **Materia:** LCDN4INT10 Inteligencia Artificial, 4o semestre
- **Bloque:** C - Toma de decisiones
- **Universidad:** Universidad Nacional Rosario Castellanos (UNRC)
- **Profesor:** Martin Humberto Llamas Haro
- **Equipo:** Stephanie Valencia, Edith Reyes
- **Programa:** Licenciatura en Ciencia de Datos para Negocios (LCDN)

## Saberes evaluados (fuente: UCA oficial)

### Declarativos (saber que)
- Teoria de la utilidad y de decisiones
- Teoria de juegos

### Procedimentales (saber hacer)
- Distinguir tipos de utilidad: ordinal, cardinal, esperada
- Representar matematicamente las preferencias de un agente
- Encontrar la solucion optima bajo riesgo e incertidumbre
- Definir un juego: jugadores, estrategias, pagos
- Construir y evaluar funciones de utilidad en juegos
- Encontrar equilibrios de Nash (puros y mixtos)

## Estructura del repositorio

```
ia-bloque-c-decisiones/
├── presentacion/
│   └── ia_bloque_c.html    ← Guia interactiva (7 tabs, quiz, defensa)
├── docs/
│   ├── contenido_bloque_c.md       ← Resumen teorico
│   └── deep_research_bloque_c.md   ← Investigacion profunda (Kimi K3)
├── references/
│   └── references.bib              ← BibTeX con fuentes primarias
├── tests/                          ← Tests si aplica
├── .github/workflows/ci.yml        ← CI pipeline
├── ARCHITECTURE.md                 ← Decisiones de arquitectura (ADRs)
├── AI_USAGE.md                     ← Transparencia en uso de IA
├── CLAUDE.md                       ← Este archivo
├── README.md                       ← Entrada principal
└── requirements.txt                ← Dependencias Python
```

## Reglas para el agente

1. **Contenido verificable:** toda afirmacion debe tener fuente. Si no hay fuente, marcar como "pendiente de verificacion"
2. **Respuestas del quiz:** cada respuesta correcta debe ser verificable contra las fuentes citadas
3. **Espanol:** todo el contenido en espanol, terminos tecnicos en ingles entre parentesis cuando sea estandar
4. **Sin LaTeX en HTML:** formulas en texto plano o HTML
5. **Accesibilidad:** tabindex, role, onkeydown en todos los elementos interactivos
6. **Dark mode:** CSS custom properties con prefers-color-scheme Y data-theme

## Fuentes primarias del bloque

| Tema | Fuente primaria |
|------|----------------|
| Axiomas VNM | von Neumann & Morgenstern (1944) |
| Equilibrio de Nash | Nash (1950), PNAS |
| Prospect Theory | Kahneman & Tversky (1979), Econometrica |
| Paradoja de Allais | Allais (1953) |
| Paradoja de Ellsberg | Ellsberg (1961) |
| Juegos y decisiones | Luce & Raiffa (1957) |
| Teoria de juegos | Osborne & Rubinstein (1994) |
| Eq. correlacionado | Aumann (1974) |
| Diseno de mecanismos | Myerson (1979/1981) |
| Libro de texto | Russell & Norvig, AIMA 4th ed., caps. 16-17 |
