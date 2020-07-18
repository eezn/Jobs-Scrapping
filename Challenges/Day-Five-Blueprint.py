import os
import requests
from bs4 import BeautifulSoup

os.system("cls")
URL = "https://www.iban.com/currency-codes"


# Using the boilerplate, make a program that gets a list of countries from a website with their currency codes, then let the user choose a country and display the currency code of that country.

# This is part one of a bigger "country scrapping" project we will complete in the following days.


def get_table():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("table", {"class": "table"}
                      ).find("tbody").find_all("tr")
    return table


def create_ncc_list(table):  # ncc = Number Country Currency
    ncc_list = []
    count = 0
    for element in table:
        each_list = str(element).split("</td>")
        if each_list[2].strip("<tr>\n<td> ") != "":
            count += 1
            local_list = []
            local_list.append(count)
            local_list.append(each_list[0].lstrip("<tr>\n<td>"))
            local_list.append(each_list[2].lstrip("<tr>\n<td>"))
            ncc_list.append(local_list)
    return ncc_list


def display_list(ncc_list):
    for each_list in ncc_list:
        print(f"# {each_list[0]} {each_list[1]}")


def find_code():
    number = input("PLEASE INPUT >>>")
    try:
        number = int(number)
        if 1 <= number <= len(ncc_list)+1:
            print(f"You choose {ncc_list[number-1][1]}")
            print(f"The currency is {ncc_list[number-1][2]}")
            restart()
        else:
            print("Choose a number from the list")
            find_code()
    except:
        print("That wasn't a number.")
        find_code()


def restart():
    answer = input("-- ONE MORE? y/n >>>")
    if answer.lower() == "y":
        # os.system('cls')
        # display_list(ncc_list)
        find_code()
    elif answer.lower() == "n":
        print("-- OKAY BYE --")


if __name__ == "__main__":
    html = get_table()
    ncc_list = create_ncc_list(html)
    display_list(ncc_list)
    find_code()


# import os
# import requests
# from bs4 import BeautifulSoup

# os.system("clear")


# url = "https://www.iban.com/currency-codes"


# countries = []

# request = requests.get(url)
# soup = BeautifulSoup(request.text, "html.parser")

# table = soup.find("table")
# rows = table.find_all("tr")[1:]

# for row in rows:
#   items = row.find_all("td")
#   name = items[0].text
#   code =items[2].text
#   if name and code:
#     if name != "No universal currency":
#       country = {
#         'name':name.capitalize(),
#         'code': code
#       }
#       countries.append(country)


# def ask():
#   try:
#     choice = int(input("#: "))
#     if choice > len(countries):
#       print("Choose a number from the list.")
#       ask()
#     else:
#       country = countries[choice]
#       print(f"You chose {country['name']}\nThe currency code is {country['code']}")
#   except ValueError:
#     print("That wasn't a number.")
#     ask()


# print("Hello! Please choose select a country by number:")
# for index, country in enumerate(countries):
#   print(f"#{index} {country['name']}")

# ask()
