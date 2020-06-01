import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=pytho&sort=i"

# 1. get the page
# 2. make the request
# 3. extract the jobs


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")  # soup -> Local Variable
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        # soup -> Local Variable
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            print(result["data-jobid"])


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
