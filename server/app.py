from flask import Flask, jsonify, request
from models import db, TodoItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = TodoItem.query.all()
    task_list = [task.to_dict() for task in tasks]
    return jsonify(task_list)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = TodoItem(text=data['text'], completed=False)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@app.route('/api/tasks/<int:id>', methods=['PATCH', 'DELETE'])
def manage_task(id):
    task = TodoItem.query.get_or_404(id)

    if request.method == 'PATCH':
        data = request.json
        task.text = data.get('text', task.text)
        task.completed = data.get('completed', task.completed)
        db.session.commit()
        return jsonify(task.to_dict())

    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
