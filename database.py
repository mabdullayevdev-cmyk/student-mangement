import json
import os

DB_FILE = "data/database.json"

def load_data():
    """Ma'lumotlar bazasidan o'quvchilar ro'yxati va ID hisoblagichini yuklash."""
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(DB_FILE):
        return [], 1
    
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            students = data.get("students", [])
            next_id = data.get("next_id", 1)
            return students, next_id
    except (json.JSONDecodeError, IOError):
        return [], 1

def save_data(students, next_id):
    """O'quvchilar ro'yxati va ID hisoblagichini JSON faylga saqlash."""
    if not os.path.exists("data"):
        os.makedirs("data")
    
    data = {
        "students": students,
        "next_id": next_id
    }
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)