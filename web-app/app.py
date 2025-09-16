from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection, init_db
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Initialize database
if not os.path.exists('database.db'):
    init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    
    if not name or not email:
        flash('Name and email are required!')
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        flash('User added successfully!')
    except sqlite3.IntegrityError:
        flash('Email already exists!')
    finally:
        conn.close()
    
    return redirect(url_for('index'))

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    flash('User deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)