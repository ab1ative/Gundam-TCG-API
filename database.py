import sqlite3
import csv

def init_db():
    conn = sqlite3.connect('gundam.db')
    c = conn.cursor()
    
    # Create the cards table
    c.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            color TEXT,
            rarity TEXT,
            level TEXT,
            cost TEXT,
            type TEXT,
            ap TEXT,
            hp TEXT,
            zone TEXT,
            trait TEXT,
            link TEXT,
            skill TEXT,
            source TEXT,
            card_number TEXT,
            edition TEXT
        )
    ''')
    
    # Load data from CSV
    with open('gundam_cards.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            c.execute('''
                INSERT INTO cards 
                (name, color, rarity, level, cost, type, ap, hp, zone, trait, link, skill, source, card_number, edition)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                row.get('Name', ''),
                row.get('Color', ''),
                row.get('Rarity', ''),
                row.get('Level', ''),
                row.get('Cost', ''),
                row.get('Type', ''),
                row.get('AP', ''),
                row.get('HP', ''),
                row.get('Zone', ''),
                row.get('Trait', ''),
                row.get('Link', ''),
                row.get('Skill', ''),
                row.get('Source', ''),
                row.get('Card #', ''),
                row.get('Edition', '')
            ))
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
