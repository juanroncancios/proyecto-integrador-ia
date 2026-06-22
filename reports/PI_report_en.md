# Proyecto Integrador - Reporte Técnico

## Introducción
Este proyecto tiene como objetivo construir un sistema que interactúe con la API de OpenAI, reciba preguntas en lenguaje natural y devuelva respuestas en formato JSON estructurado. El sistema también registra métricas de uso como tokens, latencia y costo estimado.

## Funcionamiento del script
El archivo principal `src/run_query.py`:
- Carga la clave de la API desde un archivo `.env`.
- Lee ejemplos de prompting desde `prompts/main_prompt.txt`.
- Combina esos ejemplos con la nueva pregunta del usuario.
- Envía la consulta al modelo `gpt-4o-mini`.
- Devuelve un JSON con los campos `answer`, `confidence` y `actions`.
- Registra métricas de uso y las guarda en `metrics/metrics.json`.

## Técnica de prompting
Se utilizó **few-shot prompting**, incluyendo ejemplos de preguntas y respuestas en formato JSON dentro del archivo `main_prompt.txt`. Esto asegura que el modelo mantenga consistencia en la estructura de salida.

## Métricas obtenidas
Ejemplo de ejecución:
```json
{
  "model_response": {
    "answer": "Bogotá",
    "confidence": 0.92,
    "actions": ["mostrar respuesta"]
  },
  "metrics": {
    "tokens_prompt": 30,
    "tokens_completion": 12,
    "total_tokens": 42,
    "latency_ms": 150,
    "estimated_cost_usd": 0.00042
  }
}
## Dificultades y aprendizajes
Fácil: Conectar la API y obtener respuestas básicas.

Difícil: Manejar errores de cuota y estructurar las respuestas en JSON.

Aprendizaje: La importancia de guiar al modelo con ejemplos claros y registrar métricas para evaluar el desempeño.

## Conclusión
El sistema cumple con los objetivos del Proyecto Integrador: conecta con la API de OpenAI, devuelve respuestas estructuradas en JSON, registra métricas de uso y aplica técnicas de prompting. 

## Pruebas automatizadas
Se incluyó el archivo `tests/test_core.py` para validar la estructura de las respuestas y asegurar consistencia en el formato JSON.

## Organización del repositorio
El proyecto está organizado en carpetas (`src`, `prompts`, `reports`, `tests`, `metrics`) y subido a GitHub limpio, sin secretos ni archivos sensibles.
