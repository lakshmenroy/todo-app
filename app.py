import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title('Todo List')
for idx, td in enumerate(todos):
    checkbox = st.checkbox(td, key=f"{td}-{idx}")
    if checkbox:
        todos.pop(idx)
        functions.write_todos(todos)
        del st.session_state[f"{td}-{idx}"]
        st.rerun()

st.text_input(label=' ', placeholder='Add a new item...',
              on_change=add_todo, key='new_todo')
