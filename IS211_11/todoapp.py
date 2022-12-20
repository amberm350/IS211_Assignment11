from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import re

app = Flask(__name__)

list_todo = [
    
]

@app.route('/')
def home():
    return redirect(url_for("todolist"))


@app.route('/todolist', methods = ['POST', 'GET'])
def todolist():
    return render_template('todolisttemplate.html', list_todo=list_todo)


@app.route('/submit', methods=['POST', 'GET'])
def todo():
    if request.method == 'POST':
        email = request.form['email']
        regex = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
        if (re.fullmatch(regex, email)):
            pass
        else:
            return redirect(url_for("todolist"))

        difficulty = request.form['difficulty']
        
        if(difficulty != 'low'):
            return redirect(url_for("todolist"))
        if(difficulty != 'medium'):
            return redirect(url_for("todolist"))
        if(difficulty != 'high'):
            return redirect(url_for("todolist"))
    
        else:
            todo = request.form['todolist']
            list_todo.append(todo)
            print(list_todo)
            return render_template('todolisttemplate.html', list_todo=list_todo)


@app.route('/clear')
def clearlist():
    list_todo.clear()
    return redirect(url_for("todolist"))

if __name__ == "__main__":
    app.run(debug=True)

    