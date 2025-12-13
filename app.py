# app.py
from flask import Flask, render_template, jsonify # type: ignore
import sqlite3
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
DB = "my_device_scan.db"

def query(q, args=()):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(q, args)
    rows = c.fetchall()
    conn.close()
    return rows

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/latest")
def latest():
    scan = query("SELECT id, time FROM scans ORDER BY id DESC LIMIT 1")
    if not scan:
        return jsonify({"scan_time": None, "ports": []})
    scan_id, scan_time = scan[0]
    ports = query("SELECT port, state, service FROM ports WHERE scan_id=? ORDER BY port", (scan_id,))
    return jsonify({"scan_time": scan_time, "ports": [{"port": p[0], "state": p[1], "service": p[2]} for p in ports]})

if __name__ == "__main__":
    # ensure DB exists
    if not os.path.exists(DB):
        import db as _db; _db.init_db()
    app.run(debug=True, host="127.0.0.1", port=5000)


