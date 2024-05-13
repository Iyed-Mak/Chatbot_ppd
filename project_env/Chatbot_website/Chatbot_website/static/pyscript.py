import pyodide
import pymysql




def on_click(event):
    id = event.target.parentElement.getAttribute('data')
    # delete_task_by_id(id)
    # attribute_value = button.get_attribute('data')

def runPython():
    buttons = document.querySelectorAll('.done')
    for button in buttons:
        # Bind the click event in Python using Pyodide
        button.addEventListener('click', pyodide.create_proxy(on_click))

runPython()      
