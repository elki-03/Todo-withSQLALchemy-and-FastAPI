#import todo_controller # functions only if file is named "controller"
import todo_controller
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

## GET-Read-View (all Todos)
@app.get("/")   #in url / here is endpoint of our homepage
def view_show_all_todo():    # we create a new function
      todos_dict = todo_controller.show_all_todo()
      return todos_dict

## POST-Create-View
# Pydantic, so we can check if out todo-Str is okay
class TodoCreate(BaseModel):
    task: str

@app.post("/view-new-todo")
def view_new_todo(new_todo : TodoCreate):
      todo_controller.new_todo(new_todo)
    #later exeption handling


### PUT-Update-View
## Pydantic, so we can check if out todo-Str is okay
class TodoUpdate(BaseModel):
    task: str
    
@app.put("/view-change-todo/{task_id}")
def view_change_todo(task_id: int, update_todo: TodoUpdate): # what is async?
      
      todo_controller.change_todo(task_id, update_todo)
      #--> update_todo is an instance of the TodoUpdate class no string but object with an attribute names "task"
   

## Delete-View   
@app.delete("/view-delete-todo/{task_id}")
def view_todo_controller(task_id: int):
      todo_controller.delete_todo(task_id)





