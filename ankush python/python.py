from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load quizzes from JSON file
def load_quizzes():
    with open('quizzes.json') as f:
        return json.load(f)

@app.route('/')
def index():
    quizzes = load_quizzes()
    return render_template('index.html', quizzes=quizzes)

@app.route('/quiz/<category>')
def quiz(category):
    quizzes = load_quizzes()
    selected_quiz = next((q for q in quizzes if q['category'] == category), None)
    return render_template('quiz.html', quiz=selected_quiz)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    total_questions = 0
    answers = request.form

    for key, value in answers.items():
        if value == answers[key + '_answer']:
            score += 1
        total_questions += 1

    return render_template('result.html', score=score, total=total_questions)

if __name__ == '__main__':
    app.run(debug=True)