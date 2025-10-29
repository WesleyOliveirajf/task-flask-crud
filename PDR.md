# PDR - Documento de Design do Projeto: Task Flask CRUD

## 1. Visão Geral

Este documento detalha o design e a arquitetura do projeto **task-flask-crud**. O objetivo é criar uma API RESTful para gerenciar uma lista de tarefas (To-Do). Atualmente, a aplicação armazena os dados em memória, o que significa que todas as tarefas são perdidas quando o servidor é reiniciado. O projeto parece ser parte de um curso de Flask ("curso de flask").

## 2. Stack de Tecnologia

| Componente | Tecnologia | Observações |
| :--- | :--- | :--- |
| **Linguagem** | Python | |
| **Framework** | Flask | Principal framework da aplicação. |
| **Dependências**| Werkzeug, Flask-Cors, Flask-SQLAlchemy | `Flask-SQLAlchemy` e `Flask-Cors` estão listados em `requirements.txt` mas **não são utilizados** no código atual. A aplicação usa uma lista em memória, não um banco de dados. |

## 3. Modelo de Dados e Armazenamento

### Modelo `Task`

A aplicação utiliza uma classe `Task` definida em `models/task.py` para representar as tarefas.

| Atributo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | Integer | Identificador único da tarefa. |
| `title` | String | Título da tarefa. |
| `description` | String | Descrição detalhada da tarefa. |
| `completed` | Boolean | Indica se a tarefa foi concluída. O valor padrão é `False`. |

### Armazenamento

- **Tipo:** Lista em memória (`tasks = []` em `app.py`).
- **Persistência:** Nenhuma. Os dados são voláteis e resetados a cada reinicialização da aplicação.
- **Controle de ID:** Um contador global (`task_id_control`) é usado para gerar novos IDs.

## 4. Arquitetura da API (Endpoints)

A API implementa parcialmente as operações CRUD.

### `POST /tasks` - Criar Tarefa

- **Método:** `POST`
- **Descrição:** Cria uma nova tarefa.
- **Corpo da Requisição (JSON):**
  ```json
  {
    "Title": "Título da Tarefa",
    "description": "Descrição opcional"
  }
  ```
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "messagem": "Nova tarefa criada com sucesso"
  }
  ```
- **Observação:** O campo para o título no JSON de entrada é `"Title"` (com 'T' maiúsculo), o que é inconsistente com o modelo de dados que usa `"title"`.

### `GET /tasks` - Listar Todas as Tarefas

- **Método:** `GET`
- **Descrição:** Retorna uma lista de todas as tarefas cadastradas.
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "tasks": [
      {
        "id": 1,
        "title": "Exemplo de Tarefa",
        "description": "Descrição",
        "completed": false
      }
    ],
    "total_tasks": 1
  }
  ```

### `GET /tasks/<id>` - Obter Tarefa por ID

- **Método:** `GET`
- **Descrição:** Retorna uma tarefa específica pelo seu ID.
- **Resposta de Sucesso (200 OK):** JSON com os dados da tarefa.
- **Resposta de Erro (404 Not Found):** Se a tarefa não for encontrada.
- **BUG:** A rota está definida como `/tasks/<ind: id>`, o que causa um erro. O correto seria `/tasks/<int:id>`. Além disso, o código tenta chamar `t.to_dic()`, mas o nome correto do método é `to_dict()`.

## 5. Pontos de Atenção e Sugestões de Melhoria

1.  **Bugs Críticos:**
    - A rota `GET /tasks/<id>` está quebrada devido a dois erros de digitação: `ind:` deve ser `int:` e `to_dic()` deve ser `to_dict()`.
2.  **Falta de Persistência:** A principal limitação é o uso de uma lista em memória. Sugestão: Utilizar o `Flask-SQLAlchemy` (já instalado) com um banco de dados como SQLite para tornar os dados persistentes.
3.  **Funcionalidades CRUD Incompletas:** As operações de **Update** (`PUT` ou `PATCH`) e **Delete** (`DELETE`) não foram implementadas.
4.  **Inconsistência de Nomenclatura:** O endpoint de criação espera `"Title"` (maiúsculo), enquanto o resto da aplicação usa `"title"` (minúsculo). É recomendável padronizar para minúsculo.
5.  **Dependências Não Utilizadas:** `Flask-SQLAlchemy` e `Flask-Cors` estão instalados, mas não são usados. O código deve ser atualizado para usá-los ou eles devem ser removidos do `requirements.txt` para evitar confusão.
