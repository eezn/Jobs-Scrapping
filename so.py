import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=pytho&sort=i"

# 1. get the page
# 2. make the request
# 3. extract the jobs


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    print(pages)


def get_jobs():
    last_page = get_last_page()
    return []
