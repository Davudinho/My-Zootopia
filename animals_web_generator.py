import json

# 1. JSON laden
def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

animals_data = load_data("animals_data.json")

# 2. HTML-Vorlage lesen
with open("animals_template.html", "r", encoding="utf-8") as template_file:
    html_template = template_file.read()

# 3. HTML für jedes Tier generieren
output = ""
for animal in animals_data:
    name = animal.get('name')
    locations = animal.get('locations')
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet')
    animal_type = characteristics.get('type')

    output += '<li class="cards__item">\n'
    if name:
        output += f"Name: {name}<br/>\n"
    if diet:
        output += f"Diet: {diet}<br/>\n"
    if locations and len(locations) > 0:
        output += f"Location: {locations[0]}<br/>\n"
    if animal_type:
        output += f"Type: {animal_type}<br/>\n"
    output += '</li>\n'

# 4. Platzhalter ersetzen
final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. Neue Datei speichern
with open("animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(final_html)

print("✅ animals.html wurde erfolgreich erstellt!")
