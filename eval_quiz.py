"""
eval_quiz.py - Evaluador de respuestas del quiz interactivo
============================================================
Valida que las respuestas del quiz en el HTML sean correctas
comparandolas contra un ground truth derivado de fuentes academicas.

Uso:
    python eval_quiz.py presentacion/ia_bloque_c.html
"""

import re
import sys

EXPECTED_QUESTIONS = 20

GROUND_TRUTH = {
    0: {"correct": 1, "topic": "Teoria de decisiones normativa"},
    1: {"correct": 2, "topic": "Criterio Maximin"},
    2: {"correct": 1, "topic": "Criterio de valor esperado"},
    3: {"correct": 1, "topic": "Utilidad cardinal"},
    4: {"correct": 2, "topic": "Aversion al riesgo - concavidad"},
    5: {"correct": 1, "topic": "Paradoja de San Petersburgo"},
    6: {"correct": 2, "topic": "Transitividad de utilidad"},
    7: {"correct": 1, "topic": "Componentes de un juego"},
    8: {"correct": 1, "topic": "Juegos de suma cero"},
    9: {"correct": 3, "topic": "Equilibrio de Nash en Dilema del Prisionero"},
    10: {"correct": 1, "topic": "Estrategia dominante"},
    11: {"correct": 1, "topic": "Teorema de Nash (1950)"},
    12: {"correct": 2, "topic": "Equilibrio mixto piedra/papel/tijera"},
    13: {"correct": 1, "topic": "MAUT multicriterio"},
    14: {"correct": 1, "topic": "Induccion hacia atras"},
    15: {"correct": 2, "topic": "Nash y eficiencia de Pareto"},
    16: {"correct": 1, "topic": "Reward function en RL"},
    17: {"correct": 2, "topic": "Dilema del prisionero - confianza"},
    18: {"correct": 2, "topic": "Criterio minimax regret"},
    19: {"correct": 1, "topic": "GANs como juego"},
}


def extract_quiz_answers(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    pattern = r"correct:\s*(\d+)"
    matches = re.findall(pattern, content)
    return [int(m) for m in matches]


def run_eval(html_path):
    answers = extract_quiz_answers(html_path)

    print(f"{'='*60}")
    print(f"EVAL: Quiz Bloque C")
    print(f"{'='*60}")
    print(f"Preguntas encontradas: {len(answers)}")
    print(f"Preguntas esperadas:   {EXPECTED_QUESTIONS}")
    print()

    if len(answers) != EXPECTED_QUESTIONS:
        print(f"FAIL: Se esperaban {EXPECTED_QUESTIONS} preguntas, se encontraron {len(answers)}")
        return False

    all_pass = True
    for i, answer in enumerate(answers):
        gt = GROUND_TRUTH.get(i)
        if gt is None:
            print(f"  Q{i+1:02d}: WARN - Sin ground truth")
            continue

        status = "PASS" if answer == gt["correct"] else "FAIL"
        if status == "FAIL":
            all_pass = False
            print(f"  Q{i+1:02d}: {status} - Esperado {gt['correct']}, encontrado {answer} ({gt['topic']})")
        else:
            print(f"  Q{i+1:02d}: {status} - {gt['topic']}")

    print()
    print(f"{'='*60}")
    if all_pass:
        print("RESULTADO: ALL PASS - Todas las respuestas verificadas")
    else:
        print("RESULTADO: FAIL - Hay respuestas incorrectas")
    print(f"{'='*60}")

    return all_pass


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "presentacion/ia_bloque_c.html"
    success = run_eval(path)
    sys.exit(0 if success else 1)
