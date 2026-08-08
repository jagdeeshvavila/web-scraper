import csv
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.scrapethissite.com/pages/simple/") 

with open("countries.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["country-name", "country-code", "country-capital", "country-population", "country-area", "population-density"])

    if r.status_code != 200:
        print(f"page {page} FAILED, status {r.status_code}")
    else:
        soup = BeautifulSoup(r.content, "lxml")
        countries = soup.select("div.country")

        for country in countries:
            name = country.select_one("h3.country-name").text.strip()
            flag_class = country.select_one("i.flag-icon")["class"][1]
            code = flag_class.replace("flag-icon-", "").upper()
            capital = country.select_one("span.country-capital").text
            population = int(country.select_one("span.country-population").text)
            area = float(country.select_one("span.country-area").text)
            density = round(population / area, 2) if area else 0
            writer.writerow([name, code, capital, population, area, density])

        print("done")





