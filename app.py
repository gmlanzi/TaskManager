from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "Bem-vindo ao TaskManager!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    tasks.append({"id": len(tasks) + 1, "title": data["title"]})
    return jsonify({"message": "Tarefa adicionada!"})

if __name__ == '__main__':
    app.run(debug=True)
