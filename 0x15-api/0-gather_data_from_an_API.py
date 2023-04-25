#!/usr/bin/python3

'''
    Gathers data from an API.
'''

import requests as req
from sys import argv as arg


def getData():
    '''
        Gets data from an API.
    '''
    ListOfUsers = req.get('https://jsonplaceholder.typicode.com/users').json()
    ListOfTodos = req.get('https://jsonplaceholder.typicode.com/todos').json()
    TotalTasks = 0
    TotalCompletedTasks = 0
    TaskDescription = []
    for user in ListOfUsers:
        if user.get('id') == int(arg[1]):
            Employee = user.get('name')
            break
    for todo in ListOfTodos:
        if todo.get('userId') == int(arg[1]):
            TotalTasks += 1
            if todo.get('completed') is True:
                TotalCompletedTasks += 1
                TaskDescription.append(todo.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(Employee,
                                                          TotalCompletedTasks,
                                                          TotalTasks))

    for task in TaskDescription:
        print('\t {}'.format(task))


if __name__ == '__main__':
    getData()
