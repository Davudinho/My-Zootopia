import json


# 1. JSON laden
def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


animals_data = load_data("animals_data.json")

# 2. HTML-Vorlage laden
with open("animals_template.html", "r", encoding="utf-8") as template_file:
    html_template = template_file.read()

# 3. Serialisierung: HTML-Karten erzeugen
output = ""
for animal in animals_data:
    name = animal.get('name')
    locations = animal.get('locations')
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet')
    animal_type = characteristics.get('type')

    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'

    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if locations and len(locations) > 0:
        output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'
    if animal_type:
        output += f'    <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

# 4. Platzhalter in Template ersetzen
final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. Neue Datei speichern
with open("animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(final_html)

print("✅ Neue animals.html mit Karten wurde erstellt!")
