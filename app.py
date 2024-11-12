from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar las tareas
tasks = []

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

# Ruta para agregar tareas
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('home'))

# Ruta para eliminar tareas
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
