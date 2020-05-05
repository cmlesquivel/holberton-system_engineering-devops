#!/usr/bin/python3
""" Dictionary of list of dictionaries export data in json format """

import requests
import json

if __name__ == "__main__":
    try:
        dic_json = {}
        dict_user = {}
        filename = "todo_all_employees.json"
        url_task = "https://jsonplaceholder.typicode.com/todos"
        url_user = "https://jsonplaceholder.typicode.com/users/"

        listTask = requests.get(url_task).json()
        username = requests.get(url_user).json()

        for user in username:
            dict_user[user.get("id")] = user["username"]

        for user in dict_user.keys():
            doList = []
            for item in listTask:
                if user == item["userId"]:
                    myDict = {}
                    myDict["task"] = item.get("title")
                    myDict["completed"] = item.get("completed")
                    myDict["username"] = dict_user.get(user)
                    doList.append(myDict)

            dic_json[user] = doList

        with open(filename, 'w') as file:
            json.dump(dic_json, file)

    except Exception as e:
        pass
