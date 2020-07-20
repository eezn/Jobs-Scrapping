import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("cls")
URL = "https://www.iban.com/currency-codes"

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""


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


def get_code():
    print()
    print("Where are you from? Choose a country by number.\n")
    choice = input("INPUT #: ")
    try:
        country_1 = int(country_1)
        if 1 <= country_1 <= len(ncc_list)+1:
            print(ncc_list[country_1 - 1][1])
            country_2 = to_convert()
            print(ncc_list[country_2 - 1][1])
            print()

            return convert(country_1, country_2)
            # restart()
        else:
            print("Choose a number from the list")
            get_code()
    except:
        print("That wasn't a number.")
        get_code()


def to_convert():
    print()
    print("Now choose another country.\n")
    country = input("INPUT #: ")
    try:
        country = int(country)
        if 1 <= country <= len(ncc_list)+1:
            return country

        else:
            print("Choose a number from the list")
            to_convert()
    except:
        print("That wasn't a number.")
        to_convert()


def get_rate(country_one, country_two):
    url = f"https://transferwise.com/gb/currency-converter/{country_one}-to-{country_two}-rate?amount=1"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    rate = soup.find("span", {"class": "text-success"}).get_text()
    return float(rate)


def convert(country_one, country_two):
    country1_code = ncc_list[country_one - 1][2]
    country2_code = ncc_list[country_two - 1][2]
    print(
        f"How many {country1_code} do you want to convert to {country2_code}?")
    amount = input()
    try:
        amount = int(amount)
        rate = get_rate(country1_code, country2_code)
        result = amount * rate

        return [country1_code, amount, country2_code, result]

    except:
        print("That wasn't a number.")


def restart():
    answer = input("-- ONE MORE? y/n >>>")
    if answer.lower() == "y":
        # os.system('clear')
        # display_list(ncc_list)
        get_code()
    elif answer.lower() == "n":
        print("-- OKAY BYE --")


if __name__ == "__main__":
    html = get_table()
    ncc_list = create_ncc_list(html)
    display_list(ncc_list)
    converted = get_code()

    print("{0} {1} is {2} {3}".format(
        converted[0], converted[1], converted[2], converted[3]))

    # print(format_currency(5000, "KRW", locale="ko_KR"))
    # print(type(get_rate("COP", "KRW")))
