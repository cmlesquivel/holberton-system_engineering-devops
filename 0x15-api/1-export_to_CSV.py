#!/usr/bin/python3
""" Python script to export data in the CSV format """

import requests
import sys
import csv


if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
        nameFile = str(id) + '.csv'
        url = "https://jsonplaceholder.typicode.com/users/"
        url_task = "{}{}/todos".format(url, int(sys.argv[1]))
        url_username = "{}{}/".format(url, int(sys.argv[1]))

        listTask = requests.get(url_task).json()
        username = requests.get(url_username).json().get("username")

        with open(nameFile, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)
            for item in listTask:
                spamwriter.writerow([id,
                                     username,
                                     item.get("completed"),
                                     item.get("title")])
    except Exception as e:
        pass
