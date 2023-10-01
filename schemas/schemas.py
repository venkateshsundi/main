def individual_serialiser(todo) -> dict:
    return{
        "id":str(todo["_id"]),
        "name":todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }

def list_serial(todos) -> list:
    return [individual_serialiser(todo) for todo in todos]