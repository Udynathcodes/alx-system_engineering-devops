#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import sys
import requests


def get_user_data(id):
    """
    This function fetches the data
    """
    url = f'https://jsonplaceholder.typicode.com/users/{id}/'
    apiurl = f'https://jsonplaceholder.typicode.com/users/{id}/todos'

    response = requests.get(apiurl)
    tasks = response.json()
    total_tasks = len(tasks)
    tasks_completed = 0
    title_list = []

    for task in tasks:
        if task.get('completed') is True:
            tasks_completed += 1
            title_list.append(task.get('title'))

    res = requests.get(url)
    data = res.json()
    name = data.get('name')

    print(f"Employee {name} is done with tasks({tasks_completed}/{total_tasks}): ")
    for title in title_list:
        print(f"\t {title}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_user_data(employee_id)
