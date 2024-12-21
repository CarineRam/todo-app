from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Hardcoded secret key (vulnerability)
SECRET_KEY = "mysecretkey123"

# Mock database
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')  # No input validation
    if task_content:
        tasks.append(task_content)
        return jsonify({"message": "Task added successfully!"}), 200
    return jsonify({"error": "Content cannot be empty!"}), 400

@app.route('/delete', methods=['POST'])
def delete_task():
    task_index = int(request.form.get('index'))  # No input validation
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        return jsonify({"message": "Task deleted successfully!"}), 200
    return jsonify({"error": "Invalid task index!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
