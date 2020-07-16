
# make a program that gets urls as an input and checks if they are online or not.

# The program should accept any number of URLs separated by comma, with or without 'http', with or without spaces, uppercase or lowercase. You need to handle all the cases.
# You need to check if the URL is legit or not.
# The user can restart the program after it's finished.

# strip, split, status_codes, for statements

import os
import requests

# get URLs as an input
# URLs separated by comma

# check online or not -> for, len(urls), status_codes

# with or without 'http'
# with or without spaces, uppercase or lowercase
# check if the URL is legit or not
# restart the program afther it's finished


# http://google.com, http://youtube.com, http://reddittttt.com
# google.com
# hello.com
# gggggg


def restart():
    answer = input("Do you want to start over? y/n ")
    if answer == "y":
        os.system('cls')
        is_it_down()
    elif answer == "n":
        print("Okay, bye ~")


def is_it_down():

    os.system('cls')

    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (separated by comma)")

    urls = input("is_it_down >>>").split(",")

    for url in urls:
        url = url.strip()
        if "." not in url:
            print(f"{url} is not a valid URL")
        else:
            if "http" not in url:
                url = f"http://{url}"
            try:
                response = requests.get(url)
                if response.status_code == requests.codes.ok:
                    print(f"{url} is up!")
                else:
                    print(f"{url} is down!")
            except:
                print(f"{url}, is down!")
    restart()


if __name__ == "__main__":
    is_it_down()
