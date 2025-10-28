from mailbox import NotEmptyError
from shutil import register_unpack_format
from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar e Deletar
# Tabela: Tarefa

tasks = []
task_id_control=1
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("Title"), description=data.get("description",""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"messagem": "Nova tarefa criada com sucesso"})


@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks]
  output = {
    "tasks": task_list,
    "total_tasks": len(task_list)
  }
  return jsonify(output)

@app.route('/tasks/<ind: id>', methods=['GET'])
def get_task(id):
  task = None 
  for t in tasks:
    if t.id ==id:
      return jsonify(t.to_dic())
  return jsonify({"message": "Não foi possovel encontrar a atividade"}),404
 
    
      
if __name__ == '__main__':
    app.run(debug=True) 