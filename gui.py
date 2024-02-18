import PySimpleGUI
import functions
import time

PySimpleGUI.theme('DarkPurple2')
time_now = time.strftime("%b %d, %Y %H:%M")
clock = PySimpleGUI.Text(time_now, key='clock')
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter to-do", key='todo')
add_button = PySimpleGUI.Button(size=20, image_source="media/add.png",
                                mouseover_colors='LightBlue2',
                                tooltip='Add todo', key='Add')
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button(image_source='media/complete.png',
                                     mouseover_colors='LightBlue2',
                                     tooltip='Complete todo', key='Complete')
exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window("My to-do APP",
                            layout=[[clock], [label], [input_box, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=('Helvetica', 20)
                            )

while True:
    event, values = window.read(timeout=10000)
    window['clock'].update(value=time_now)

    print(event)
    print(values)

    if event == 'Add':
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":
        try:
            edit_todo = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            PySimpleGUI.popup("Please, select an item first",
                              font=('Helvetica', 20))

    elif event == "Complete":
        try:
            complete_todo = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(complete_todo)
            todos.pop(index)

            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(values="")
        except IndexError:
            PySimpleGUI.popup("Please, select an item first",
                              font=('Helvetica', 20))

    elif event == 'Exit':
        break

    elif event == 'todos':
        window['todo'].update(value=values['todos'][0])

    elif event == PySimpleGUI.WIN_CLOSED:
    # else:
        break

window.close()
