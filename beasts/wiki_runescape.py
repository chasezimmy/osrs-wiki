from bs4 import BeautifulSoup, NavigableString


def fetch(html, url):

    soup = BeautifulSoup(html, 'html.parser')
    drop_tables = soup.find_all(class_='item-drops')

    name = soup.find(class_='firstHeading').text
    rare_drop_table = soup.find(class_='rdtable') is not None
    url = url
    img = "https://oldschool.runescape.wiki" + soup.find(class_="infobox-image").find('img')['src'] if soup.find(class_="infobox-image") else None

    drops = []

    drop_key = {0: 'img', 1: 'name', 2: 'quantity', 3: 'rarity', 4: 'ge'}

    if len(drop_tables) == 0:
        drop_tables = soup.find_all(class_='dtable')

        for drop_table in drop_tables:
            for trs in drop_table:
                if isinstance(trs, NavigableString):
                    continue
                tds = trs.find_all('td')
                drop = {}
                for i, td in enumerate(tds):

                    if i % 5 == 4:
                        drops.append(drop)
                        drop = {}
                        continue

                    element = None
                    if td.find('img'):
                        element = "https://oldschool.runescape.wiki" + td.find('img')['src']
                    elif "[" in td.text:
                        element = td.text[:td.text.find('[')].strip()
                    elif td:
                        element = td.text.strip()

                    drop[drop_key[i%5]] = element
    else:
        for drop_table in drop_tables:
            for trs in drop_table.find_all('tr'):
                drop = {}
                td = trs.find_all('td')

                if len(td) == 0:
                    continue

                drop['img'] = "https://oldschool.runescape.wiki" + td[0].find('img')['src'] if td[0] else None
                drop['name'] = td[1].text.strip() if td[1] else None
                drop['quantity'] = td[2].text.strip() if td[2] else None
                drop['rarity'] = td[3].text[:td[3].text.find('[')].strip() if "[" in td[3].text else td[3].text.strip() if td[3] else None
                drops.append(drop)

    return {
        name: {
            'drops': drops,
            'rare_drop_table': rare_drop_table,
            'url': url,
            'img': img
        }
    }
