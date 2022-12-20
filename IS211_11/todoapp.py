from flask import Flask
from flask import render_template
from flask import request, redirect, url_for


app = Flask(__name__)

list_todo = [
    
]

@app.route('/')
def home():
    print(list_todo)
    return redirect(url_for("todolist"))


@app.route('/todolist', methods = ['POST', 'GET'])
def todolist():
    if request.method =='POST':
        task = request.values.get('task')
        email = request.values.get('email')
        difficulty = request.values.get('difficulty')
        
        
        if ('@' not in email):
            return redirect(url_for("todolist"))
    
        
        list_todo.append({"task": task, "email" : email,"difficulty": difficulty})
        
    return render_template('todolisttemplate.html', list_todo=list_todo)

@app.route('/clear')
def clearlist():
    list_todo.clear()
    return redirect(url_for("todolist"))
    
if __name__ == "__main__":
    app.run(debug=True)

    