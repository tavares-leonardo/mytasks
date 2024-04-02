from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect('mytasks.db')

@app.route('/')
def index():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/insert', methods=['POST'])
def insert():
    description = request.form['description']
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description) VALUES(?)', (description,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
