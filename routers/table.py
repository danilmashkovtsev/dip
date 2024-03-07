from fastapi import APIRouter

table = APIRouter()

# Создаем фейковую базу данных
fake_db = [
    {"id": 1, "lung": 4, "hearth": 3, "spleen": 2, "liver": 1, "pericardium": 5, "kidney": 4}
]

@table.get("/{element}/{criterion}")
async def get_element_organs(element: str, criterion: int):

    result = fake_db[0]

    # Создаем словарь органов
    organs = {
        "lung": result["lung"],
        "hearth": result["hearth"],
        "spleen": result["spleen"],
        "liver": result["liver"],
        "pericardium": result["pericardium"],
        "kidney": result["kidney"]
    }

    # Создаем пустой список для подходящих органов
    element_organs = []

    # Определяем органы, соответствующие стихии и критерию
    for organ in organs:
        if result[organ] == criterion:
            element_organs.append(organ)

    # Возвращаем список подходящих органов или пустой список, если органов не найдено
    return {f"{element}_organs": element_organs}