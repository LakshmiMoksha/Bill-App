from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
from flask import flash


app = Flask(__name__)
app.secret_key = 'jimin-chimmy'


# Initialize DB
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            items TEXT,
            total REAL,
            date TEXT
        )
    ''')
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    customer_name = request.form['customer_name']
    items = request.form.getlist('item[]')
    prices = request.form.getlist('price[]')
    quantities = request.form.getlist('quantity[]')

    total = 0
    bill_items = []

    for item, price, qty in zip(items, prices, quantities):
        line_total = float(price) * int(qty)
        bill_items.append(f"{item} (x{qty}) - ₹{line_total}")
        total += line_total

    # Save to DB
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO bills (customer_name, items, total, date) VALUES (?, ?, ?, ?)", 
                 (customer_name, "\n".join(bill_items), total, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

    return render_template('bill.html', customer=customer_name, items=bill_items, total=total)

@app.route('/bills')
def view_bills():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bills ORDER BY date DESC")
    bills = cur.fetchall()
    conn.close()
    return render_template('bills_list.html', bills=bills)
@app.route('/delete/<int:bill_id>', methods=['POST'])
def delete_bill(bill_id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM bills WHERE id = ?", (bill_id,))
    conn.commit()
    conn.close()
    flash("Bill deleted successfully!", "success")
    return redirect(url_for('view_bills'))


if __name__ == '__main__':
    app.run(debug=True)
