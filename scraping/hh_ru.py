import asyncio
import time

from scraping.module.functions import __, con, __exc, turn, get_url__KomBo
from bs4 import BeautifulSoup
import lxml
from work_ua import main_work


def find_vocancy__hh(response, language, index, domen, __domen, x):
    soup = BeautifulSoup(response.text, "lxml")
    try:
        all_vocancy = soup.find("div", class_="vacancy-serp-content").find_all("div", class_="serp-item")
    except Exception:
        all_vocancy = []
    if index > len(con) - 1:
        turn["index"] = index
        con.append([language, len(all_vocancy), list(), dict(), turn["index"], "hh.json"])
    if all_vocancy:
        turn["index"] = index
        for items in all_vocancy:
            try:
                __("title", items.find("h3", class_="bloko-header-section-3").find("span").find("a").text)
                __("url", items.find("h3", class_="bloko-header-section-3").find("span").find("a").get("href"))
                __("description", '\n'.join([content.text for content in items.find("div", class_="g-user-content")
                                            .find_all("div", class_="bloko-text")]).replace(" ", "").replace("⁠", ""))
                __("company", items.find("a", class_="bloko-link_kind-tertiary").text.
                   replace(" ", "").replace("⁠", ""))
                __("city", items.find("div", class_="vacancy-serp-item__info").find_all("div", class_="bloko-text")[-1].text
                   .replace(" ", "").replace("⁠", ""))
            except Exception:
                continue



#loop = asyncio.get_event_loop()
#
start = time.time()
#try:
#    asyncio.wait(loop.create_task(*[get_url(find_vocancy,"https://hh.ru", "python", page=page) for page in range(20)]))
#except Exception:
#    pass
#















