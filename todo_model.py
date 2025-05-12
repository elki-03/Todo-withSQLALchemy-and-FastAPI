
from sqlalchemy import create_engine
#creating or connect new sql-file()
# engine = create_engine("sqlite://todo.db", echo = True)

engine = create_engine("sqlite:///todo.db", echo=True)

#define table
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base ##makes a new Baseclass for all SQLAlchemy-Models

#ORM-> so we can work with db items like with get_objects

Base = declarative_base() #base class for all tables (declarative_base makes is so)

class Todo(Base): #our table is names Todo, inherits from Base. Todo is automaticly made into an SQL table by SQLAlchemy
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True)
    task = Column(String)
    
    #representation-method
    def __repr__(self):
        return f"Todo:  id={self.id}, task='{self.task}'" #no ' on id coz int
    
#create Table in db (which tables were defined (Todo) creates them in SQLite db)
Base.metadata.create_all(engine)

# functions for db actions
from sqlalchemy.orm import Session

session = Session (engine) #new session for insert and queries

#read (all) and make them to a dict for the view
def read_all_todo():
    all_todos = session.query(Todo).all()
    # for todo in all_todos:
    #     print(todo)
    todos_dict = [{"id": todo.id, "task": todo.task} for todo in all_todos]

    #for table to be correctly shown, we need a __repr__-method (do not forget!)
    return todos_dict

#create
def create_todo(new_todo):
    # new_todo = Todo(task = new_todo)
    # Aber new_todo ist nicht einfach nur ein String, sondern eine Instanz der Klasse TodoCreate. Du musst daher auf das task-Attribut zugreifen. Korrigiere die Zeile so:
    new_todo = Todo(task=new_todo.task)
    
    #add to session and save
    session.add(new_todo)
    session.commit()
    return

#update
def update_todo(task_id, update_todo):
    todo = session.query(Todo).filter_by(id=task_id).first()  # Fetch first Todo with id=1

    if todo:
        #todo.task = update_todo  # change item to what user wrote into variable "change"--> console version()
        todo.task = update_todo.task  # Attribute Access (update_todo is a complete object and task its attribute)
        session.commit()  # Speichere die Änderung in der Datenbank
        return
            
#delete
def delete_todo(task_id):
    todo = session.query(Todo).filter_by(id=task_id).first() # Fetch first Todo with id=1
    if todo:
        session.delete(todo)
        session.commit()
    return