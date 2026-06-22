```python
import src.run_query as rq

def test_response_structure():
    result = rq.generate_response("¿Cuál es la capital de Francia?")
    assert "answer" in result["model_response"]
    assert "confidence" in result["model_response"]