#!/usr/bin/python3
'''
    Gathers data from an API.
'''

import requests as req
import sys
#importing libraries 


def getData():
    '''
        Gets data from an API.
    '''
    response_users = req.get('https://jsonplaceholder.typicode.com/users')
    response_todos = req.get('https://jsonplaceholder.typicode.com/todos')
    response_users.raise_for_status()
    response_todos.raise_for_status()
    ListOfUsers = response_users.json()
    ListOfTodos = response_todos.json()
    TotalTasks = 0
    TotalCompletedTasks = 0
    TaskDescription = [todo.get('title') for todo in ListOfTodos if todo.get('userId') == int(sys.argv[1])]
    Employee = next((user.get('name') for user in ListOfUsers if user.get('id') == int(sys.argv[1])), None)
    if Employee is None:
        print('Employee not found')
        return
    TotalTasks = len(TaskDescription)
    TotalCompletedTasks = sum(1 for todo in ListOfTodos if todo.get('userId') == int(sys.argv[1]) and todo.get('completed'))
    print(f'Employee {Employee} is done with tasks({TotalCompletedTasks}/{TotalTasks}):')
    for task in TaskDescription:
        print(f'\t {task}')

if __name__ == '__main__':
    getData()
