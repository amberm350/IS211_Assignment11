from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

list_todo = []
list_todo.append("We need to buy groceries")
list_todo.append("We need to mow the lawn")
list_todo.append("We need to wash the dishes")

@app.route('/')
def to_do_list():
    return render_template('todolisttemplate.html')


@app.route('/todolist')
def more_hello():
    return 'This is a list of things to do'


@app.route('/todolist/')
@app.route('/todolist/<username>')
def helloname(username=None):
    return render_template('todolisttemplate.html', name=username)


@app.route('/todolist', methods=['POST', 'GET'])
def todolist():
    if request.method == 'POST':
        todo = request.form['todolist']
        list_todo.append(todo)
        print(list_todo)
        return render_template('todolisttemplate.html', name=request.form['username'])


if __name__ == "__main__":
    app.run()

    