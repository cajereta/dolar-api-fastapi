import gc

import requests
from bs4 import BeautifulSoup


def scrap_site():
    url = "https://www.cronista.com/MercadosOnline/dolar.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    with requests.get(url, headers=headers) as r:
        soup = BeautifulSoup(r.content, "html5lib")

    target_names = ["Dólar BNA", "Dólar Blue", "Dólar turista"]
    results = {}

    target_rows = [
        row
        for row in soup.find_all("td", class_="name")
        if row.find("a").text.strip() in target_names
    ]
    for row in target_rows:
        name = row.find("a").text.strip()
        sell_value_td = row.find_next_sibling("td", class_="sell")
        sell_value = sell_value_td.find("div", class_="sell-value").get_text(strip=True)
        cleaned_sell_value = float(
            sell_value.replace("$", "").replace(".", "", 1).replace(",", ".").strip(),
        )

        results[name] = cleaned_sell_value

    date_td = soup.find("td", class_="date")
    if date_td:
        updated_text = date_td.get_text(strip=True)
        updated_time = updated_text.split("Última actualización")[-1].split()[0]

    gc.collect()

    return results, updated_time
