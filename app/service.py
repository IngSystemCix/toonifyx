from python_toon import convert_json_to_toon

def json_to_toon(data: dict):
    try:
        result = convert_json_to_toon(data)
        return result
    except Exception as e:
        return {"error": str(e)}