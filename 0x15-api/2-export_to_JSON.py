#!/usr/bin/python3
""" Python script to export data in the JSON format """

import requests
import sys
import json

if __name__ == "__main__":
    try:
        doList = []
        dic_json = {}
        id = sys.argv[1]
        filename = id + '.json'
        url = "https://jsonplaceholder.typicode.com/users/"
        url_task = "{}{}/todos".format(url, int(id))
        url_name = "{}{}/".format(url, int(id))

        listTask = requests.get(url_task).json()
        username = requests.get(url_name).json()["username"]

        for item in listTask:
            myDict = {}
            myDict["task"] = item["title"]
            myDict["completed"] = item["completed"]
            myDict["username"] = username
            doList.append(myDict)

        dic_json[id] = doList

        with open(filename, 'w') as file:
            json.dump(dic_json, file)

    except Exception as e:
        pass
