import src.run_query as rq

def test_response_structure():
    result = rq.generate_response("¿Cuál es la capital de Francia?")
    assert "answer" in result["model_response"]
    assert "confidence" in result["model_response"]
    assert "actions" in result["model_response"]
    assert isinstance(result["model_response"]["answer"], str)
    assert isinstance(result["model_response"]["confidence"], float)
    assert isinstance(result["model_response"]["actions"], list)

def test_response_colombia():
    result = rq.generate_response("¿Cuál es la capital de Colombia?")
    assert result["model_response"]["answer"] == "Bogotá"
    assert "confidence" in result["model_response"]
    assert "actions" in result["model_response"]
