from flask import Flask, request, jsonify
from controllers.task_controller import TaskController

app = Flask(__name__)
controller = TaskController()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = controller.list_tasks()
    tasks_list = [
        {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed
        }
        for task in tasks
    ]
    return jsonify(tasks_list), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    title = data['title']
    description = data.get('description', '')

    task = controller.add_task(title, description)

    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed
    }), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = controller.find_task(task_id)

    if not task:
        return jsonify({'error': 'Task not found'}), 404

    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed
    }), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = controller.find_task(task_id)

    if not task:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()

    if 'completed' in data:
        if data['completed']:
            controller.mark_completed(task_id)
        else:
            task.mark_uncompleted()
            controller.save_tasks()

    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed
    }), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if controller.delete_task(task_id):
        return jsonify({'message': 'Task deleted'}), 200

    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
