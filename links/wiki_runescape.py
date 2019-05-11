from bs4 import BeautifulSoup
from requests_html import HTMLSession


def levels():

    level_urls = [
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_1_to_10",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_11_to_20",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_21_to_30",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_31_to_40",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_41_to_50",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_51_to_60",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_61_to_70",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_71_to_80",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_81_to_90",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_91_to_100",
        "https://oldschool.runescape.wiki/w/Bestiary/Levels_higher_than_100"
    ]

    beast_links = []
    session = HTMLSession()
    for url in level_urls:
        r = session.get(url=url)
        beast_links += fetch(r.content)

    return beast_links


def fetch(html):
    """
    read level pages, get beasts
    :return: list of beast links
    """
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find(class_="mw-content-ltr")

    links = []
    for td in body.find_all('td'):
        a = td.find('a')
        if a:
            if a.text not in ["Magic", "Melee", "Ranged", "Dragonfire", "melee", "Typeless magical ranged", "Magical ranged", "Magic-based melee", "Typeless", "Range", "magic", "Magical melee", "Typeless magic", "Free-to-play"]:
                if "File:" not in a['href']:
                    links.append("https://oldschool.runescape.wiki" + a['href'])

    if links:
        return links

    links = []
    for n in body.find_all('li'):
        if n.find('a'):
            slug = n.find('a').get('href', '')
            if "#" not in slug and "Bestiary" not in slug and slug:
                links.append("https://oldschool.runescape.wiki" + slug)

    return links
