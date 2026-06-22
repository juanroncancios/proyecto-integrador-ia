import json
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar la API key desde .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(user_query: str) -> dict:
    """
    Llama al modelo de OpenAI y devuelve respuesta en JSON.
    """

    # Leer el archivo de prompt con ejemplos
    with open("prompts/main_prompt.txt", "r", encoding="utf-8") as f:
        base_prompt = f.read()

    # Combinar el prompt con la nueva pregunta
    prompt = base_prompt + f"\nPregunta: {user_query}"

    start_time = time.time()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    latency_ms = int((time.time() - start_time) * 1000)
    output_text = completion.choices[0].message.content

    try:
        response_json = json.loads(output_text)
    except:
        response_json = {"answer": output_text, "confidence": 0.5, "actions": []}

    final_result = {
        "model_response": response_json,
        "metrics": {
            "tokens_prompt": completion.usage.prompt_tokens,
            "tokens_completion": completion.usage.completion_tokens,
            "total_tokens": completion.usage.total_tokens,
            "latency_ms": latency_ms,
            "estimated_cost_usd": round(completion.usage.total_tokens * 0.00001, 5)
        }
    }

    # Crear carpeta metrics si no existe
    os.makedirs("metrics", exist_ok=True)

    # Guardar métricas en archivo JSON (una línea por ejecución)
    with open("metrics/metrics.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(final_result, ensure_ascii=False) + "\n")

    print(json.dumps(final_result, indent=4, ensure_ascii=False))
    return final_result

if __name__ == "__main__":
    test_query = "¿Cómo puedo recuperar mi contraseña de la billetera digital?"
    generate_response(test_query)
