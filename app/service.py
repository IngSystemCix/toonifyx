from toon import encode

def json_to_toon(data: dict):
    try:
        result = encode(data)
        return result
    except Exception as e:
        return {"error": str(e)}