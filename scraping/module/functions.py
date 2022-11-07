import json


from fake_useragent import UserAgent
import requests


con = []
turn = {}


def __(key=None, value=None, end=None, constant=con, delpth=5, _path=None, _return=False, **kwargs):
    if key and not kwargs:
        language, _end, list_vocany, _dict, index, path = constant[turn["index"]]
        _dict[key] = value if value else {i: kwargs.get(i) for i in kwargs}
        if len(_dict) == delpth:
                list_vocany.append(_dict)
                _dict = {}
                if constant:
                    constant[index][3] = {}
    if kwargs:
        __errors = kwargs
        print(__errors)
    if _return:
        try:
            file_path = _path if _path else constant[turn["index"]][-1]
            with open(file_path, "w", encoding="utf-8") as file:
                dump_list = [i[2] for i in constant if i[-1] == file_path and i[2]]
                json.dump(dump_list, file, indent=4, ensure_ascii=False)
                result = dump_list
                print(result)
            return constant
        except IndexError as exc:
            print(exc)




def __exc(url, headers, path="errors.json"):
    try:
        response = requests.get(url=url, headers=headers)
        print(url)
        if response.status_code != 200:
            __(path=path, key="errors", end=1, delpth=1, title=url, content="сайт не отвечает",
               stats_code=response.status_code)

    except Exception as exc:
        __(path=path, key="errors", end=1, delpth=1, title=url, content="сайт не отвечает")
        response = None
    return response


def get_url__KomBo(func, domen_serch, text, language, city="", page=0, index=None, __domen=None, x=None):
    user_agent = UserAgent()
    headers = {"user-agent": f"{user_agent.random}"}
    domen = domen_serch
    city = city
    __domen = __domen
    language = language
    url = f"{domen}{text}{language}{x}page={page}"
    response = __exc(url, headers)
    if response:
        func(response, language, index, domen, __domen, x)



def html_send_file(context, template_name="email_template.html"):
    html = '''<!doctype html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
        </head>
    <body>'''
    for _context in context:
        title = _context.title
        url = _context.url
        description = _context.description
        timer = _context.timer.strftime("%d %B, %Y")
        city = _context.city
        company = _context.company
        __html = f'''<div style="
                      min-width: 200px;
                      width: 700px;
                      height: 220px;
                      margin: 10px auto;
                      background: -webkit-linear-gradient(45deg, rgb(255, 12, 65), rgb(15, 15, 15) 10%, rgb(114, 53, 104) 100%);
                      background: -moz-linear-gradient(45deg, rgb(255, 12, 65), rgb(15, 15, 15) 10%, rgb(114, 53, 104) 100%);
                      background: linear-gradient(45deg, rgb(255, 12, 65), rgb(15, 15, 15) 10%, rgb(114, 53, 104) 100%);
                      opacity: 0.9;
                      border-radius: 33px;
                      text-align: left;
                      -webkit-box-shadow: -9px 11px 76px 38px rgba(0, 255, 97, 0.49);
                      -moz-box-shadow: -9px 11px 76px 38px rgba(0, 255, 97, 0.49);
                      box-shadow: -9px 11px 76px 38px rgba(0, 255, 97, 0.49);">
                    <a href='{url}' style = "text-decoration: none;">
                        <h3 style="
                              color: white;
                              text-shadow: 1px 1px 1px #fb0071f2, 0 0 35px #c300fff2, 0 0 50px #ff1100f2;
                              margin: 0px auto;
                              text-align: center;
                              font-weight: bolder;
                              inline-size: 600px;
                              ">'{title}'
                        </h3>
                    </a>
                    <p style="
                        padding: 0px 10px;
                        color: white;
                        margin-bottom: 10px;">'{description}'
                    </p>
                        <p style="        
                      margin-bottom: 3px;
                      margin-top: 2px;
                      padding: 0 10px;
                      margin: 2px 10px;
                      padding: 0px;
                      color: white;
                      padding-left: 1px;
                    "
                    >{city}</p>
                    <p style="
                    margin-top: 2px;
                     padding: 0px 10px;
                     color: white;
                     padding-left: 9px;
                     margin-bottom: 5px;">{company}</p>
                    <h5 class="timer" style="
                        padding-bottom: 17px;
                        color: white;
                        margin-top: 0px;
                        padding-left: 9px;
                        font-weight: bolder"">
                        {timer}
                    </h5>
                </div>\n'''
        html+=__html
    html += "</body> " \
            "</html>"
    with open(template_name, "w", encoding='utf-8') as file:
        file.write("".join(html))
