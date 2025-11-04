import json

# 1. JSON-Datei laden
def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

animals_data = load_data("animals_data.json")

# 2. HTML-Vorlage lesen
with open("animals_template.html", "r", encoding="utf-8") as template_file:
    html_template = template_file.read()

# 3. String mit Tierinformationen erzeugen
animals_output = ""

for animal in animals_data:
    name = animal.get('name')
    locations = animal.get('locations')
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet')
    animal_type = characteristics.get('type')

    if name:
        animals_output += f"Name: {name}\n"
    if diet:
        animals_output += f"Diet: {diet}\n"
    if locations and len(locations) > 0:
        animals_output += f"Location: {locations[0]}\n"
    if animal_type:
        animals_output += f"Type: {animal_type}\n"

    animals_output += "\n"  # Leerzeile nach jedem Tier

# 4. Platzhalter in HTML ersetzen
final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_output)

# 5. Neue Datei animals.html speichern
with open("animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(final_html)

print("✅ Datei 'animals.html' wurde erfolgreich erstellt!")
