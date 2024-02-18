import streamlit
import functions

todos = functions.get_todos()


def add_todo():
    todo = streamlit.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


streamlit.title('My todo app')
streamlit.subheader('This is my todo app')

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit.rerun()

streamlit.text_input("", placeholder='Add new todo',
                     on_change=add_todo, key='new_todo')


streamlit.session_state