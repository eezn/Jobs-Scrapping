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


# import os
# import requests

# def restart():
#   answer = str(input("Do you want to start over? y/n ")).lower()
#   if answer == "y" or answer =="n":
#     if answer == "n":
#         print("k. bye!")
#         return
#     elif answer == "y":
#       main()
#   else:
#     print("That's not a valid answer")
#     restart()


# def main():
#   os.system('clear')
#   print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
#   urls = str(input()).lower().split(",")
#   for url in urls:
#     url = url.strip()
#     if "." not in url:
#       print(url, "is not a valid URL.")
#     else:
#       if "http" not in url:
#         url = f"http://{url}"
#       try:
#         request = requests.get(url)
#         if request.status_code == 200:
#           print(url,"is up!")
#         else:
#           print(url, "is down!")
#       except:
#           print(url, "is down!")
#   restart()


# main()
