import json


def load_data(file_path):
    """
    Loads and returns JSON data from a file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def serialize_animal(animal_obj):
    """
    Converts a single animal object into an HTML <li> string.
    """
    name = animal_obj.get("name", "Unknown")
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})

    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")
    location = locations[0] if locations else "Unknown"

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {diet}<br/>\n'
    output += f'    <strong>Location:</strong> {location}<br/>\n'
    output += f'    <strong>Type:</strong> {animal_type}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_html(data):
    """
    Iterates over animal objects and returns the full HTML list as a string.
    """
    output = ""
    for animal in data:
        output += serialize_animal(animal)
    return output


def main():
    # 1. JSON-Daten laden
    animals_data = load_data("animals_data.json")

    # 2. HTML-Vorlage lesen
    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        html_template = template_file.read()

    # 3. Tierdaten → HTML generieren
    animals_html = generate_animals_html(animals_data)

    # 4. Platzhalter ersetzen
    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # 5. Datei speichern
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(final_html)

    print("✅ Datei 'animals.html' wurde erfolgreich erstellt!")


if __name__ == "__main__":
    main()
