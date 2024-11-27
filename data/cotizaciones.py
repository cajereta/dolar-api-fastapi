import asyncio
from datetime import datetime

from utils.scrap import scrap_site

data = {"cotizaciones": {}, "actualizado": ""}


async def fetch_data():
    print("Fetching initial data...")
    results, updated_time = scrap_site()
    data["cotizaciones"] = results
    data["actualizado"] = updated_time


async def refresh_data():
    while True:
        current_hour = datetime.now().hour
        if 8 <= current_hour <= 21:
            await fetch_data()
            await asyncio.sleep(1800)
        else:
            print("Outside active hours, data not refreshed...")
            await asyncio.sleep(3600)
