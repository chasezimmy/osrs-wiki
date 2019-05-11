import json
from requests_html import HTMLSession
from links import wiki_runescape as links
from beasts import wiki_runescape as beasts
from test import test

if __name__ == '__main__':

    with open('bestiary.json', 'r') as f:
        bestiary = json.load(f)
    session = HTMLSession()
    links = links.levels()

    for i, link in enumerate(links):
        r = session.get(url=link)
        print(link, r.status_code)
        beast = beasts.fetch(r.content, r.url)

        bestiary.update(beast)

        with open('bestiary.json', 'w') as outfile:
            json.dump(bestiary, outfile)
