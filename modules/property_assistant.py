def suggest_property(budget, location):
    properties = [
        {"name": "Casa Jardines del Río", "price": 650000, "location": "Tamazunchale"},
        {"name": "Depto Centro", "price": 720000, "location": "Tamazunchale"},
        {"name": "Casa San Rafael", "price": 890000, "location": "Ciudad Valles"}
    ]
    return [p for p in properties if p["price"] <= budget and location.lower() in p["location"].lower()]
