import psycopg2
from config import DB_CONFIG

def init_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Create table for storing image-question-answer interactions
    cur.execute('''
    CREATE TABLE IF NOT EXISTS interactions (
        id SERIAL PRIMARY KEY,
        image_path TEXT NOT NULL,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def save_interaction(image_path, question, answer):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # Insert interaction into the database
    cur.execute('''
    INSERT INTO interactions (image_path, question, answer) VALUES (%s, %s, %s)
    ''', (image_path, question, answer))
    
    conn.commit()
    cur.close()
    conn.close()
