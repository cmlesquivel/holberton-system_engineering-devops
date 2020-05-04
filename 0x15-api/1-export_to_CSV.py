#!/usr/bin/python3
""" Python script to export data in the CSV format """

import requests
import sys
import csv


if __name__ == "__main__":
    try:
        id = sys.argv[1]
        nameFile = id + '.csv'
        url = "https://jsonplaceholder.typicode.com/users/"
        url_task = "{}{}/todos".format(url, int(sys.argv[1]))
        url_username = "{}{}/".format(url, int(sys.argv[1]))

        listTask = requests.get(url_task).json()
        username = requests.get(url_username).json()["username"]

        with open(nameFile, 'w', newline='') as csvfile:
            fieldnames = ["USER_ID",
                          "USERNAME",
                          "TASK_COMPLETED_STATUS",
                          "TASK_TITLE"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for item in listTask:
                writer.writerow({'USER_ID': id,
                                 'USERNAME': username,
                                 'TASK_COMPLETED_STATUS': item["completed"],
                                 'TASK_TITLE': item["title"]})
    except Exception as e:
        pass