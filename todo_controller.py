import todo_model as model

#mit Callback
def show_all_todo():
    #through model: get all items out of sqlitedb
    todos_dict = model.read_all_todo()
    #print in view
    #return # weil sonst fehler :/
    return todos_dict

def new_todo(new_todo):
    #new_task = input("Write new to-do item:\n")
    #name in model-> model: in sqlite
    model.create_todo(new_todo)
    
    #print in view "to-do was put in list (maybe updated list with read/show all to do)"
    return

    
def change_todo(task_id, update_todo):
    #task_id = input("Type id of the Todo you want to change")
    #change = input ("Type the changed expression of the To-do item")
    #ask forname or id --> through model get item
    model.update_todo(task_id, update_todo)
    
    
    #after update --> back to model + update through model
    
    #if successful (try except) show view "successful"
    #maybe updated list with read/show all to do
    return

def delete_todo(task_id):
    #ask for name or id --> through model delete item
    
    #if successful (try except) show view "successful"
    #maybe updated list with read/show all to do
    
    #task_id = input("Type id of the Todo you want to delete")
    #ask forname or id --> through model get item
    model.delete_todo(task_id)



