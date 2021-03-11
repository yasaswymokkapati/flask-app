from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        'id' : 1, 
        'contact' : 9395559131,
        'name' : 'Amma',
        'done' : False
    },
    {
        'id' : 2,
        'contact' : 9866911174,
        'name' : 'Nanna',
        'done' : False
    }
]
@app.route('/add-data', methods = ['POST'])
def add_task():
    if not request.json :
        return jsonify({
            'status' : 'error',
            'message' : 'Please provide the data',
        }, 400)
    task = {
        'id' : tasks[-1]['id']+1,
        'contact' : request.json['contact'],
        'name' : request.json.get('name', ''),
        'done' : False
    }
    tasks.append(task)
    return jsonify({
        'status' : 'success',
        'message' : 'Task added successfully'
    })
@app.route('/get-data')
def get_task():
    return jsonify({
        'data' : tasks
    })
@app.route("/")
def hello_world():
    return "Hello World"
if __name__ == '__main__':
    app.run(debug = True)