#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """

import requests
import sys

if __name__ == "__main__":
    try:
        doList = []
        url = "https://jsonplaceholder.typicode.com/users/"
        url_task = "{}{}/todos".format(url, sys.argv[1])
        url_name = "{}{}/".format(url, sys.argv[1])
        listTask = requests.get(url_task).json()
        name = requests.get(url_name).json()["name"]
        mystr = "is done with tasks"

        for item in listTask:
            if item["completed"] is True:
                doList.append(item["title"])

        print("{} {} ({}/{}):".format(name, mystr, len(doList), len(listTask)))
        for i in doList:
            print("\t {}".format(i))
    except Exception as e:
        pass
