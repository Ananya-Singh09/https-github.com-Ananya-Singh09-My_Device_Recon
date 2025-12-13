# db.py
import sqlite3

DB = "my_device_scan.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS scans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TEXT
    );
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS ports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scan_id INTEGER,
        port INTEGER,
        state TEXT,
        service TEXT
    );
    """)

    conn.commit()
    conn.close()

def add_scan(time):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO scans(time) VALUES(?)", (time,))
    conn.commit()
    sid = c.lastrowid
    conn.close()
    return sid

def add_port(scan_id, port, state, service):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "INSERT INTO ports(scan_id, port, state, service) VALUES(?,?,?,?)",
        (scan_id, port, state, service)
    )
    conn.commit()
    conn.close()
