#!/usr/bin/python3

'''
    Exports data from an API and stores as a JSON file.
'''

if __name__ == "__main__":
    import json
    from requests import get

    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in get(url + "todos",
                           params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
