import sqlite3
import os
import base64
from flask import Flask, jsonify, request as req

app = Flask(__name__)

# Initialize database if it doesn't exist
if not os.path.exists('gundam.db'):
    import database
    database.init_db()

def get_db():
    conn = sqlite3.connect('gundam.db')
    conn.row_factory = sqlite3.Row
    return conn

def row_to_dict(row):
    return {
        "id": row["id"],
        "name": row["name"],
        "color": row["color"],
        "rarity": row["rarity"],
        "level": row["level"],
        "cost": row["cost"],
        "type": row["type"],
        "ap": row["ap"],
        "hp": row["hp"],
        "zone": row["zone"],
        "trait": row["trait"],
        "link": row["link"],
        "skill": row["skill"],
        "source": row["source"],
        "card_number": row["card_number"],
        "edition": row["edition"]
    }

def sync_to_github():
    token = os.environ.get('GITHUB_TOKEN')
    repo = os.environ.get('GITHUB_REPO')
    path = os.environ.get('GITHUB_CSV_PATH')

    print(f"Token present: {bool(token)}")
    print(f"Repo: {repo}")
    print(f"Path: {path}")
    
    if not token or not repo or not path:
        print("GitHub sync not configured — skipping")
        return
    
    # Get all cards from database
    conn = get_db()
    rows = conn.execute("SELECT * FROM cards").fetchall()
    conn.close()
    
    # Write to CSV string
    import io
    import csv as csv_module
    output = io.StringIO()
    writer = csv_module.DictWriter(output, fieldnames=[
        'Name', 'Color', 'Rarity', 'Level', 'Cost', 'Type',
        'AP', 'HP', 'Zone', 'Trait', 'Link', 'Skill',
        'Source', 'Card #', 'Edition'
    ])
    writer.writeheader()
    for row in rows:
        writer.writerow({
            'Name': row['name'],
            'Color': row['color'],
            'Rarity': row['rarity'],
            'Level': row['level'],
            'Cost': row['cost'],
            'Type': row['type'],
            'AP': row['ap'],
            'HP': row['hp'],
            'Zone': row['zone'],
            'Trait': row['trait'],
            'Link': row['link'],
            'Skill': row['skill'],
            'Source': row['source'],
            'Card #': row['card_number'],
            'Edition': row['edition']
        })
    
    csv_content = output.getvalue()
    encoded = base64.b64encode(csv_content.encode('utf-8')).decode('utf-8')
    
    # Get current file SHA (required by GitHub API to update a file)
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github+json'
    }
    url = f'https://api.github.com/repos/{repo}/contents/{path}'
    response = req.get(url, headers=headers)
    sha = response.json().get('sha')
    
    # Commit updated CSV
    req.put(url, headers=headers, json={
        'message': 'Auto-update card data via API',
        'content': encoded,
        'sha': sha
    })
    result = req.put(url, headers=headers, json={
        'message': 'Auto-update card data via API',
        'content': encoded,
        'sha': sha
    })
    print(f"GitHub sync response: {result.status_code} {result.text}")
    print("Synced to GitHub successfully.")

@app.route('/cards', methods=['GET'])
def get_cards():
    color = request.args.get('color')
    card_type = request.args.get('type')
    name = request.args.get('name')
    
    query = "SELECT * FROM cards WHERE 1=1"
    params = []
    
    if color:
        query += " AND LOWER(color) = LOWER(?)"
        params.append(color)
    if card_type:
        query += " AND LOWER(type) = LOWER(?)"
        params.append(card_type)
    if name:
        query += " AND LOWER(name) LIKE LOWER(?)"
        params.append(f"%{name}%")
    
    conn = get_db()
    cards = [row_to_dict(row) for row in conn.execute(query, params)]
    conn.close()
    return jsonify(cards)

@app.route('/cards/<int:card_id>', methods=['GET'])
def get_card(card_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
    conn.close()
    if not row:
        return jsonify({"error": "Card not found"}), 404
    return jsonify(row_to_dict(row))

@app.route('/cards', methods=['POST'])
def create_card():
    data = request.json
    conn = get_db()
    conn.execute('''
        INSERT INTO cards (name, color, rarity, level, cost, type, ap, hp, zone, trait, link, skill, source, card_number, edition)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('name', ''),
        data.get('color', ''),
        data.get('rarity', ''),
        data.get('level', ''),
        data.get('cost', ''),
        data.get('type', ''),
        data.get('ap', ''),
        data.get('hp', ''),
        data.get('zone', ''),
        data.get('trait', ''),
        data.get('link', ''),
        data.get('skill', ''),
        data.get('source', ''),
        data.get('card_number', ''),
        data.get('edition', '')
    ))
    conn.commit()
    new_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (new_id,)).fetchone()
    conn.close()
    sync_to_github()
    return jsonify(row_to_dict(row)), 201

@app.route('/cards/<int:card_id>', methods=['PUT'])
def update_card(card_id):
    data = request.json
    conn = get_db()
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
    if not row:
        conn.close()
        return jsonify({"error": "Card not found"}), 404
    conn.execute('''
        UPDATE cards SET
            name = ?,
            color = ?,
            rarity = ?,
            level = ?,
            cost = ?,
            type = ?,
            ap = ?,
            hp = ?,
            zone = ?,
            trait = ?,
            link = ?,
            skill = ?,
            source = ?,
            card_number = ?,
            edition = ?
        WHERE id = ?
    ''', (
        data.get('name', row['name']),
        data.get('color', row['color']),
        data.get('rarity', row['rarity']),
        data.get('level', row['level']),
        data.get('cost', row['cost']),
        data.get('type', row['type']),
        data.get('ap', row['ap']),
        data.get('hp', row['hp']),
        data.get('zone', row['zone']),
        data.get('trait', row['trait']),
        data.get('link', row['link']),
        data.get('skill', row['skill']),
        data.get('source', row['source']),
        data.get('card_number', row['card_number']),
        data.get('edition', row['edition']),
        card_id
    ))
    conn.commit()
    updated = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
    conn.close()
    sync_to_github()
    return jsonify(row_to_dict(updated))

@app.route('/cards/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
    if not row:
        conn.close()
        return jsonify({"error": "Card not found"}), 404
    conn.execute("DELETE FROM cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    sync_to_github()
    return jsonify({"message": f"Card {card_id} deleted successfully"}), 200

@app.route('/sets', methods=['GET'])
def get_sets():
    conn = get_db()
    rows = conn.execute("SELECT DISTINCT source FROM cards WHERE source != '' ORDER BY source").fetchall()
    conn.close()
    return jsonify([row['source'] for row in rows])

@app.route('/sets/<set_code>/cards', methods=['GET'])
def get_set_cards(set_code):
    conn = get_db()
    rows = conn.execute("SELECT * FROM cards WHERE LOWER(source) = LOWER(?)", (set_code,)).fetchall()
    conn.close()
    if not rows:
        return jsonify({"error": "Set not found"}), 404
    return jsonify([row_to_dict(row) for row in rows])

if __name__ == '__main__':
    app.run(debug=True)
