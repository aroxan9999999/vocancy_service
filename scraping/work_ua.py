import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from scraping.module.functions import __, con, __exc, get_url, turn
import lxml
from fake_useragent import UserAgent


headers, domen, city, language = get_url("https://www.work.ua", "java")
url = f"{domen}/ru/jobs-{city}{language}"


def main_work(exc):
    response = exc
    if response:
          soup = BeautifulSoup(response.text, "lxml")
          main_div = soup.find("div", id="pjax-job-list")
          if not main_div:
              __(path="work_ua.json", key="errors", end=1, delpth=1, title=url, content="сайт не отвечает")
          else:
              _list = main_div.find_all("div", class_="job-link")
              con.append([len(_list), list(), dict(), turn["index"], "work_ua.json"])
              for items in _list:
                  _items = items.find("h2")
                  __("title", _items.a.get("title"))
                  __("url", domen + _items.a.get('href'))
                  __("content", '\n'.join([i.lstrip() for i in items.p.text.split("\n")]).replace(" ", "").replace("⁠", "")
                     .replace("\n", ""))
                  __("company", items.img.get("alt") if items.find("img") else None)



main_work(__exc(url, headers, "work_ua.json"))









