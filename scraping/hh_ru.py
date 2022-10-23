import asyncio
import time

from scraping.module.functions import __, con, get_url, __exc, turn
from bs4 import BeautifulSoup
import lxml




def main_hh():
    start = time.time()
    respone = __exc("SDS", "ASDAS", "hh.json")
    if True:
        soup = BeautifulSoup(respone.text, "lxml")
        all_vocancy = soup.find("div", class_="vacancy-serp-content").find_all("div", class_="serp-item")
        turn["index"] = 0
        con.append([len(all_vocancy), list(), dict(), turn["index"], "hh.json"])
        print(len((all_vocancy)))
        for items in all_vocancy:
            try:
                __("title", items.find("h3", class_="bloko-header-section-3").find("span").find("a").text)
                __("url", items.find("h3", class_="bloko-header-section-3").find("span").find("a").get("href"))
                print(items.find("div", class_="g-user-content"))
                __("description", '\n'.join([content.text for content in items.find("div", class_="g-user-content")
                                        .find_all("div", class_="bloko-text")]).replace(" ", "").replace("⁠", ""))
                __("company", items.find("a", class_="bloko-link_kind-tertiary").text.
                   replace(" ", "").replace("⁠", ""))
            except Exception:
                continue
    end_time = time.time() - start
    print(end_time)




def find_vocancy(response=None):
    soup = BeautifulSoup(response.text, "lxml")
    all_vocancy = soup.find("div", class_="vacancy-serp-content").find_all("div", class_="serp-item")
    turn["index"] = 0
    con.append([len(all_vocancy), list(), dict(), turn["index"], "hh.json"])
    for items in all_vocancy:
        try:
            __("title", items.find("h3", class_="bloko-header-section-3").find("span").find("a").text)
            __("url", items.find("h3", class_="bloko-header-section-3").find("span").find("a").get("href"))
            __("description", '\n'.join([content.text for content in items.find("div", class_="g-user-content")
                                        .find_all("div", class_="bloko-text")]).replace(" ", "").replace("⁠", ""))
            __("company", items.find("a", class_="bloko-link_kind-tertiary").text.
               replace(" ", "").replace("⁠", ""))
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
for page in range(20):
    get_url(find_vocancy,"https://hh.ru", "python", page=page)
end = time.time() - start
print(end)














