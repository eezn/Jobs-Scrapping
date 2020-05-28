import os
import requests


def is_it_down():

    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (sparated by comma)")

    url_list = map(str, input(">>>").split(','))

    for item in url_list:
        url = item.strip(' htp:/w.')
        result = requests.get("http://{0}".format(url))
        # print(url, result)

        if result.status_code == requests.codes.ok:
            print("{0} is up!".format(item.strip()))
        else:
            print("{0} is down!".format(item.strip()))

    answer = input("Do you want to start over? y/n ")
    if answer == "y":
        os.system('cls')
        is_it_down()
    elif answer == "n":
        print("Okay, bye!")


if __name__ == "__main__":
    is_it_down()
