import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from scraping.module.functions import __, con, __exc, turn, get_url__KomBo
import lxml
from fake_useragent import UserAgent

from scraping.module.functions import __, con, __exc, turn, get_url__KomBo


def main_work(response, language, index, domen, __domen, x):
    soup = BeautifulSoup(response.text, "lxml")
    main_div = soup.find("div", id="pjax-job-list")
    if main_div:
        _list = main_div.find_all("div", class_="job-link")
        if index > len(con) - 1:
            turn["index"] = index
            con.append([language, len(_list), list(), dict(), turn["index"], "work_ua.json"])
        for items in _list:
            try:
                _items = items.find("h2")
                __("title", _items.a.get("title"))
                __("url", __domen + _items.a.get('href'))
                __("content", '\n'.join([i.lstrip() for i in items.p.text.split("\n")]).replace(" ", "").replace("⁠", "")
                   .replace("\n", ""))
                __("company", items.img.get("alt") if items.find("img") else None, delpth=4)
            except Exception as exc:
                print(exc)











