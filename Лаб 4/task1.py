# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_product = sum(item["score"] * item["weight"] for item in data)
    return round(total_product, 3)

print(task())
