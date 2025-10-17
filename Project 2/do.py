from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory task storage
tasks = []

@app.route('/')
def index():
    return render_template('do.html', tasks=tasks)

@app.route('/', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
