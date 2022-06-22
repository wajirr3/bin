import httpx
import random
from bs4 import BeautifulSoup as bs


async def ua_scrape():
    page = random.randint(2,64)
    url = f'https://m.gsmarena.com/samsung-phones-{page}.php'
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            soup = bs(r, features='html.parser')
            k = soup.findAll('strong')
            m = random.choice(k)
            data = {}
            data["status"] = True
            data["ua"] = f'Mozilla/5.0 (Android {random.randint(10,12)}; Mobile; {m.get_text()}; rv:101.0) Gecko/101.0 Firefox/101.0'.strip()
            return data
    except Exception as e:
        return {"status": False, "error": e}
