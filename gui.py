import functions
import PySimpleGUI as sg
import time

sg.theme("Darkteal12")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events= True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
query = sg.Text(key="text_under")
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, query]],
                   font=('Helvetica', 20))
pls2e = 0
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if pls2e == 1:
        window['text_under'].update(value="")
        pls2e = pls2e - 1
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                window['text_under'].update(value="Please select a todo to edit.", font=("Helvetica", 20))
                if pls2e == 0:
                    pls2e = pls2e + 1


        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                window['text_under'].update(value="Please select todo to complete.", font=("Helvetica", 20))
                if pls2e == 0:
                    pls2e = pls2e + 1
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

print("program terminated")
window.close()