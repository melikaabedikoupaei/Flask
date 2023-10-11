from flask import Flask, request, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#without html
''' @app.route('/')
def index():
    return "hello word"
if __name__ == '__main__':
    app.run(debug=True)
 '''
#with html
''' @app.route('/')
def index():
    return render_template ('index1.html')
if __name__ == '__main__':
    app.run(debug=True)
 ''' 
#with css 
'''  @app.route('/')
def index():
    return render_template ('index2.html')
if __name__ == '__main__':
    app.run(debug=True)

  '''
  
  
#with database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    completed=db.Column(db.Integer,default=0)
    data_created=db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return '<task %r>' %self.id


    
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        task_content=request.form['content']
        new_task=Todo(content=task_content)
        
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    else:
        tasks=Todo.query.order_by(Todo.data_created).all()
        return render_template ('index3.html',tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete=Todo.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    

  

  
  
  