import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("cls")
alba_url = "http://www.alba.co.kr"


def get_brand():
    request = requests.get(alba_url)
    soup = BeautifulSoup(request.text, "html.parser")
    superbrand = soup.find("div", {"id": "MainSuperBrand"}).find(
        "ul", {"class": "goodsBox"}).find_all("li")
    brand_list = []
    for brand in superbrand:
        company = brand.find("span", {"class": "company"}).string
        link = brand.find("a").get("href")
        brand_list.append({"company": company, "link": f"{link}job/brand/"})

    return brand_list


def get_details(list):
    count = 0
    for job in list:
        count += 1
        company = job["company"]
        request = requests.get(job["link"])
        soup = BeautifulSoup(request.text, "html.parser")
        try:
            rows = soup.find("tbody").find_all("tr")
            print(f"{count}/{len(list)} {company}")
            details = []
            for row in rows:
                if row.find("td", {"class": "local"}):
                    try:
                        place = row.find("td", {"class": "local"}).text
                        title = row.find("span", {"class": "company"}).text
                        time = row.find("span", {"class": "time"}).text
                        pay = row.find("td", {"class": "pay"}).text
                        date = row.find("td", {"class": "regDate"}).text
                        detail = {
                            "place": place,
                            "title": title,
                            "time": time,
                            "pay": pay,
                            "date": date
                        }

                        details.append(detail)

                    except AttributeError:
                        detail = {
                            "place": None,
                            "title": None,
                            "time": None,
                            "pay": None,
                            "date": None
                        }

                        details.append(detail)

            save_to_file(details, company)

        except:
            pass


def save_to_file(details, company):
    try:
        if not (os.path.isdir("csv_files")):
            os.makedirs(os.path.join("csv_files"))
    except OSError as e:
        if e.errno != e.errno.EEXIST:
            print("Failed to create directory!")
            raise
    file = open(f"csv_files/{company}.csv", encoding='utf-8-sig', mode="w")
    writer = csv.writer(file)
    writer.writerow(["plance", "title", "time", "pay", "date"])
    for detail in details:
        writer.writerow(list(detail.values()))


if __name__ == "__main__":
    brands = get_brand()
    details = get_details(brands)
