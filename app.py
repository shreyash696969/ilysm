from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('responses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS responses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, heading TEXT, emotions TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Route for the first question page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the second question
@app.route('/question_two')
def question_two():
    return render_template('question_two.html')

# Route for the popup "Your Life is Precious" page
@app.route('/precious_life')
def precious_life():
    return render_template('precious_life.html')

# Route for the main page with three text boxes
@app.route('/main_page')
def main_page():
    return render_template('main_page.html')

# Route for the Express Your Feelings page
@app.route('/express')
def express():
    return render_template('express.html')

# Route for saving responses
@app.route('/save_response', methods=['POST'])
def save_response():
    heading = request.form['heading']
    emotions = request.form['emotions']
    conn = sqlite3.connect('responses.db')
    c = conn.cursor()
    c.execute("INSERT INTO responses (heading, emotions) VALUES (?, ?)", (heading, emotions))
    conn.commit()
    conn.close()
    return redirect(url_for('acknowledgment'))

# Route for showing acknowledgment page
@app.route('/acknowledgment')
def acknowledgment():
    return render_template('acknowledgment.html')

# Route for showing saved responses
@app.route('/responses')
def saved_responses():
    conn = sqlite3.connect('responses.db')
    c = conn.cursor()
    c.execute("SELECT heading, emotions FROM responses")
    responses = c.fetchall()
    conn.close()
    return render_template('responses.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True)
