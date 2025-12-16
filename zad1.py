def create_greeting(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


greeting = create_greeting("Jan", "Kowalski")
print(greeting)
