import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load card data from CSV
cards = []
with open('gundam_cards.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cards.append(row)

@app.route('/cards', methods=['GET'])
def get_cards():
    color = request.args.get('color')
    card_type = request.args.get('type')
    name = request.args.get('name')
    results = cards
    if color:
        results = [c for c in results if c['Color'].lower() == color.lower()]
    if card_type:
        results = [c for c in results if c['Type'].lower() == card_type.lower()]
    if name:
        results = [c for c in results if name.lower() in c['Name'].lower()]
    return jsonify(results)

@app.route('/cards/<card_name>', methods=['GET'])
def get_card(card_name):
    result = [c for c in cards if c['Name'].lower() == card_name.lower()]
    if not result:
        return jsonify({"error": "Card not found"}), 404
    return jsonify(result)

@app.route('/sets', methods=['GET'])
def get_sets():
    sets = list(set(c['Source'] for c in cards if c['Source']))
    return jsonify(sorted(sets))

@app.route('/sets/<set_code>/cards', methods=['GET'])
def get_set_cards(set_code):
    result = [c for c in cards if c['Source'].upper() == set_code.upper()]
    if not result:
        return jsonify({"error": "Set not found"}), 404
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)