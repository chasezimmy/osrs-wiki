import json
from requests_html import HTMLSession
from links import wiki_runescape as links
from beasts import wiki_runescape as beasts


if __name__ == '__main__':
    beasts.fetch(None, "https://oldschool.runescape.wiki/w/Duck")
"""
    bestiary = {}
    session = HTMLSession()
    links = links.fetch()

    for link in links:
        r = session.get(url=link)
        print(link)
        beast = beasts.fetch(r.content, r.url)
        bestiary.update(beast)

    with open('bestiary.json', 'w') as outfile:
        json.dump(bestiary, outfile)
"""
    # scrape links

    # loop through links /beasts

    # save giant json obj

