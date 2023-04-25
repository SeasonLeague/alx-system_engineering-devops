#!/usr/bin/python3

'''
    Exports data from an API and stores as a JSON    file.
'''

if __name__ == "__main__":
    import json
    from requests import get
    from sys import argv, exit

    try:
        id = argv[1]
        checkType = int(id)
    except Exception:
        exit()

    User = "https://jsonplaceholder.typicode.com/users?id={}".format(id)
    Todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)

    user = get(User)
    todo = get(Todo)

    try:
        Employee = user.json()
        Tasks = todo.json()
    except ValueError:
        print("Not a valid JSON.")

    if Employee and Tasks:
        EmployeeID = id
        EmployeeName = Employee[0].get("username")

        jsonList = []
        for task in Tasks:
            TaskStatus = task.get("completed")
            TaskTitle = task.get("title")

            dictInfo = {
                "task": TaskTitle,
                "completed": TaskStatus,
                "username": EmployeeName
            }
            jsonList.append(dictInfo)
        data = {EmployeeID: jsonList}

        with open("{}.json".format(id), "w", newline='') as jsonfile:
            json.dump(data, jsonfile)
